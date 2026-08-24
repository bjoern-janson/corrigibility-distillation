#!/usr/bin/env python3
"""RD-001 pre-learner apparatus: generator, R0, R*, BFS, counter, calibration.
No R_L learner or learner design is implemented here.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from collections import defaultdict, deque
from hashlib import sha256
from itertools import permutations
import argparse, json

P=4; NVAL=(7,8,9); KVAL=(3,4,5)

def bit(d,j): return (d>>j)&1
def proj(d,J): return tuple(bit(d,j) for j in J)
def pspace(n,k):
    z=1
    for i in range(k): z*=n-i
    return z

class RNG:
    def __init__(self,seed): self.seed=seed; self.c=0; self.buf=b''
    def _fill(self):
        self.buf+=sha256(self.seed+self.c.to_bytes(8,'big')).digest(); self.c+=1
    def take(self,n):
        while len(self.buf)<n: self._fill()
        x,self.buf=self.buf[:n],self.buf[n:]; return x
    def u64(self): return int.from_bytes(self.take(8),'big')
    def below(self,n):
        L=(1<<64)-((1<<64)%n)
        while True:
            x=self.u64()
            if x<L:return x%n
    def choice(self,x): return x[self.below(len(x))]
    def shuffle(self,x):
        for i in range(len(x)-1,0,-1):
            j=self.below(i+1); x[i],x[j]=x[j],x[i]
    def sample(self,x,k):
        y=list(x); self.shuffle(y); return y[:k]

@dataclass(frozen=True,order=True)
class Edge:
    u:int; v:int; j:int=-1; b:int=-1
    @property
    def label(self): return 'FREE' if self.j<0 else f'B{self.j}={self.b}'

@dataclass(frozen=True)
class Trap:
    a:int; b:int; src:int; dst:int; spare:int; j:int; value:int
    state_a:tuple[int,...]; state_b:tuple[int,...]

@dataclass(frozen=True)
class Inst:
    role:str; index:int; candidate:int; n:int; k:int
    ids:tuple[str,...]; desc:tuple[int,...]; J:tuple[int,...]
    edges:tuple[Edge,...]; initial:tuple[int,...]; goals:tuple[int,...]
    trap:Trap; layout_hash:str

class Count:
    def __init__(self): self.d=defaultdict(int)
    def add(self,k,n=1): self.d[k]+=n
    @property
    def total(self): return sum(self.d.values())
    def snap(self): return dict(sorted(self.d.items()))

def outs(I):
    d=defaultdict(list)
    for e in I.edges:d[e.u].append(e)
    return {u:tuple(sorted(es)) for u,es in d.items()}

def isgoal(I,s,c=None):
    if c:c.add('goal_position_read',I.k);c.add('goal_set_build',I.k);c.add('goal_compare',I.k)
    return frozenset(s)==frozenset(I.goals)

def allowed(I,s,t,e,c=None):
    if c:c.add('successor_attempt');c.add('position_read');c.add('occupancy_scan',I.k)
    if s[t]!=e.u or e.v in s:return False
    if e.j>=0:
        if c:c.add('descriptor_read');c.add('gate_check')
        if bit(I.desc[t],e.j)!=e.b:return False
    return True

def succ(I,s,c=None):
    O=outs(I)
    for t in range(I.k):
        if c:c.add('token_position_read')
        for e in O.get(s[t],()):
            if allowed(I,s,t,e,c):
                q=list(s)
                if c:c.add('state_copy_atom',I.k);c.add('state_write');c.add('successor_generated')
                q[t]=e.v; yield (t,e.u,e.v),tuple(q)

class R0:
    name='R0'
    def inst(self,I,c): c.add('instantiate_native_token_record',I.k); return None
    def key(self,I,s,x,c):
        z=[]
        for i in range(I.k):
            c.add('key_identity_read');c.add('key_position_read');c.add('key_descriptor_read')
            z+=(I.ids[i],s[i],I.desc[i]); c.add('key_atom_emit',3);c.add('hash_mix',3)
        return tuple(z)

class RStar:
    name='R_STAR'
    def inst(self,I,c):
        cls=[]
        for d in I.desc:
            q=[]
            for j in I.J:c.add('instantiate_descriptor_read');q.append(bit(d,j))
            c.add('instantiate_class_assign');cls.append(tuple(q))
        labs=tuple(sorted(set(cls)));c.add('instantiate_class_label_sort_compare',max(0,len(labs)-1))
        return tuple(cls),labs
    def _sort(self,a,c):
        a=list(a)
        for i in range(1,len(a)):
            x=a[i];j=i-1
            while j>=0:
                c.add('canonical_compare')
                if a[j]<=x:break
                a[j+1]=a[j];c.add('canonical_move');j-=1
            a[j+1]=x;c.add('canonical_write')
        return tuple(a)
    def key(self,I,s,x,c):
        cls,labs=x; buckets={q:[] for q in labs}
        for i in range(I.k):
            c.add('key_class_read');c.add('key_position_read');c.add('bucket_insert');buckets[cls[i]].append(s[i])
        z=[]
        for q in labs:
            c.add('key_class_label_emit');c.add('hash_mix');z.append(q)
            for v in self._sort(buckets[q],c):c.add('key_atom_emit');c.add('hash_mix');z.append(v)
        return tuple(z)

@dataclass
class Search:
    solved:bool; actions:list; n_states:int; n_generated:int; n_expanded:int; n_duplicates:int
    c_instantiate:int; c_search:int; c_verify:int; verified:bool
    instantiate_counts:dict; search_counts:dict; verify_counts:dict
    @property
    def c_fresh(self):return self.c_instantiate+self.c_search+self.c_verify

def verify(I,acts,claimed):
    c=Count();s=I.initial;O=outs(I);ok=True
    for t,u,v in acts:
        c.add('verify_action');e=None
        for z in O.get(u,()):
            c.add('verify_edge_scan')
            if z.v==v:e=z;break
        if e is None or t>=I.k or s[t]!=u or not allowed(I,s,t,e,c):ok=False;break
        q=list(s);c.add('verify_state_copy_atom',I.k);c.add('verify_state_write');q[t]=v;s=tuple(q)
    c.add('verify_goal_call');g=isgoal(I,s,c)
    return ok and ((claimed and g) or ((not claimed) and not g)),c

def bfs(I,R):
    ci=Count();x=R.inst(I,ci);cs=Count();start=I.initial;k0=R.key(I,start,x,cs)
    seen={k0};cs.add('visited_lookup');cs.add('visited_insert');Q=deque([(k0,start)]);cs.add('queue_push')
    parent={};native={k0:start};ng=ne=nd=0;kg=None
    while Q:
        cs.add('queue_pop');k,s=Q.popleft();ne+=1
        if isgoal(I,s,cs):kg=k;break
        for a,t in succ(I,s,cs):
            ng+=1;kt=R.key(I,t,x,cs);cs.add('visited_lookup')
            if kt in seen:nd+=1;cs.add('duplicate_detect');continue
            seen.add(kt);cs.add('visited_insert');parent[kt]=(k,a);native[kt]=t;Q.append((kt,t));cs.add('queue_push')
    acts=[]
    if kg is not None:
        k=kg
        while k!=k0:cs.add('path_parent_lookup');k,a=parent[k];acts.append(a)
        acts.reverse();cs.add('path_reverse',len(acts))
    vv,cv=verify(I,acts,kg is not None)
    return Search(kg is not None,acts,len(seen),ng,ne,nd,ci.total,cs.total,cv.total,vv,ci.snap(),cs.snap(),cv.snap())

def rstar_key_plain(I,s):
    cls=tuple(proj(d,I.J) for d in I.desc);labs=sorted(set(cls));B={q:[] for q in labs}
    for i,v in enumerate(s):B[cls[i]].append(v)
    return tuple((q,tuple(sorted(B[q]))) for q in labs)

def structural(I):
    K=set(rstar_key_plain(I,s) for s in permutations(range(I.n),I.k));return pspace(I.n,I.k),len(K)

def trap_ok(I,R):
    c=Count();x=R.inst(I,c);ka=R.key(I,I.trap.state_a,x,c);kb=R.key(I,I.trap.state_b,x,c)
    if ka==kb:return False
    e=next(z for z in I.edges if (z.u,z.v,z.j,z.b)==(I.trap.src,I.trap.dst,I.trap.j,I.trap.value))
    return allowed(I,I.trap.state_a,I.trap.a,e) and not allowed(I,I.trap.state_b,I.trap.b,e)

def layouthash(n,edges,initial,goals):
    z={'n':n,'edges':[(e.u,e.v,e.j,e.b) for e in sorted(edges)],'initial':sorted(initial),'goals':sorted(goals)}
    return sha256(json.dumps(z,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def trapstates(k,n,a,b,src,dst,spare):
    rest=[v for v in range(n) if v not in {src,dst,spare}];q=[None]*k;q[a]=src;q[b]=spare;r=0
    for t in range(k):
        if q[t] is None:q[t]=rest[r];r+=1
    A=tuple(q);B=list(A);B[a],B[b]=B[b],B[a];return A,tuple(B)

def candidate(r,role,idx,cand):
    n=r.choice(NVAL);k=r.choice(tuple(x for x in KVAL if x<n));J=tuple(sorted(r.sample(range(P),1+r.below(2))));irr=[j for j in range(P) if j not in J]
    base=r.below(16);safe=base
    for j in irr:safe^=1<<j
    bad=base
    for j in J:bad^=1<<j
    desc=[base,safe,bad]
    while len(desc)<k:desc.append(r.below(16))
    ids=tuple(f'{role}-{idx:03d}-T{i+1}' for i in range(k));perm=list(range(n));r.shuffle(perm);initial=tuple(perm[:k])
    off=max(2,n//2);goals=tuple(sorted({perm[(off+i)%n] for i in range(k)}))
    if len(goals)!=k:goals=tuple(sorted(perm[-k:]))
    E=set()
    for i in range(n):u,v=perm[i],perm[(i+1)%n];E.add(Edge(u,v));E.add(Edge(v,u))
    target=2*n+2+r.below(3)
    while sum(e.j<0 for e in E)<target:
        u,v=r.sample(range(n),2);E.add(Edge(u,v))
    non=[v for v in range(n) if v not in initial];gates=[]
    for j in J:
        for _ in range(100):
            u=r.choice(non);v=r.below(n)
            if u==v or Edge(u,v) in E:continue
            e=Edge(u,v,j,bit(base,j));E.add(e);gates.append(e);break
        else:raise RuntimeError('gate placement failed')
    g=gates[0];sp=r.choice([v for v in range(n) if v not in (g.u,g.v)]);A,B=trapstates(k,n,0,2,g.u,g.v,sp)
    T=Trap(0,2,g.u,g.v,sp,g.j,g.b,A,B);lh=layouthash(n,E,initial,goals)
    return Inst(role,idx,cand,n,k,ids,tuple(desc),J,tuple(sorted(E)),initial,goals,T,lh)

def valid(I):
    if proj(I.desc[0],I.J)!=proj(I.desc[1],I.J) or I.desc[0]==I.desc[1]:return False
    for j in range(P):
        if j not in I.J and bit(I.desc[0],j)==bit(I.desc[1],j):return False
    for j in I.J:
        if not any(e.j==j for e in I.edges) or {bit(d,j) for d in I.desc}!={0,1}:return False
    if not trap_ok(I,RStar()):return False
    z=bfs(I,R0());return z.solved and z.verified

def suite(seed,role,count,excluded=()):
    r=RNG(sha256(seed+role.encode()).digest());out=[];seen=set(excluded);cand=0
    while len(out)<count:
        if cand>100000:raise RuntimeError('rejection limit')
        I=candidate(r,role,len(out),cand);cand+=1
        if I.layout_hash in seen or not valid(I):continue
        seen.add(I.layout_hash);out.append(I)
    return out

def enc(I):
    return {'role':I.role,'index':I.index,'candidate':I.candidate,'n':I.n,'k':I.k,'ids':list(I.ids),'desc':[format(d,'04b') for d in I.desc],
            'edges':[{'u':e.u,'v':e.v,'label':e.label} for e in I.edges],'initial':list(I.initial),'goals':list(I.goals),'layout_hash':I.layout_hash,
            'oracle':{'J':list(I.J),'trap':asdict(I.trap)}}
def dec(d):
    E=[]
    for x in d['edges']:
        if x['label']=='FREE':E.append(Edge(x['u'],x['v']))
        else:a,b=x['label'].split('=');E.append(Edge(x['u'],x['v'],int(a[1:]),int(b)))
    t=d['oracle']['trap'];T=Trap(t['a'],t['b'],t['src'],t['dst'],t['spare'],t['j'],t['value'],tuple(t['state_a']),tuple(t['state_b']))
    return Inst(d['role'],d['index'],d['candidate'],d['n'],d['k'],tuple(d['ids']),tuple(int(x,2) for x in d['desc']),tuple(d['oracle']['J']),tuple(sorted(E)),tuple(d['initial']),tuple(d['goals']),T,d['layout_hash'])

def calibrate(S):
    rows=[];a=b=0;ok0=oks=tr=True
    for I in S:
        n0,ns=structural(I);x=bfs(I,R0());y=bfs(I,RStar());tt=trap_ok(I,RStar());ok0&=x.solved and x.verified;oks&=y.solved and y.verified;tr&=tt;a+=x.c_fresh;b+=y.c_fresh
        rows.append({'instance':I.index,'layout_hash':I.layout_hash,'n':I.n,'k':I.k,'J':list(I.J),'state_R0':n0,'state_R_STAR':ns,'state_ratio':n0/ns,
                     'R0':asdict(x)|{'c_fresh':x.c_fresh},'R_STAR':asdict(y)|{'c_fresh':y.c_fresh,'trap_preserved':tt},'lambda_fresh':x.c_fresh/y.c_fresh,'delta_search':x.c_search-y.c_search,'delta_fresh':x.c_fresh-y.c_fresh})
    gate=oks and tr and b<a
    return {'experiment':'RD-001','phase':'PRE_LEARNER_AVAILABLE_LEVERAGE_CALIBRATION','count':len(S),'aggregate':{'sum_C_fresh_R0':a,'sum_C_fresh_R_STAR':b,'aggregate_lambda_fresh':a/b,'delta_C_fresh':a-b,'R0_all_correct':ok0,'R_STAR_all_correct':oks,'R_STAR_all_traps_preserved':tr,'available_leverage_gate':gate,'verdict':'AVAILABLE_LEVERAGE_DEMONSTRATED' if gate else 'AVAILABLE_LEVERAGE_NOT_DEMONSTRATED / LEARNER_NOT_DESIGNED'},'rows':rows}

def derive(randomness,prereg,tag):
    b=bytes.fromhex(randomness);h=bytes.fromhex(prereg)
    if len(b)!=32 or len(h)!=20 or tag not in ('RD001/CAL','RD001/TRAIN','RD001/TEST'):raise ValueError('bad seed inputs')
    return sha256(b+h+tag.encode()).digest()

def selftest():
    seed=sha256(b'RD001 NONSCIENTIFIC SELFTEST').digest();S=suite(seed,'DEV',5);assert len({x.layout_hash for x in S})==5
    for I in S:
        assert proj(I.desc[0],I.J)==proj(I.desc[1],I.J);assert trap_ok(I,RStar());assert bfs(I,R0()).verified;assert bfs(I,RStar()).verified;assert structural(I)[1]<structural(I)[0]
    A=calibrate(S);B=calibrate(suite(seed,'DEV',5));assert A==B
    assert derive('11'*32,'22'*20,'RD001/CAL')==sha256(bytes.fromhex('11'*32)+bytes.fromhex('22'*20)+b'RD001/CAL').digest()
    print('RD001 SELFTEST PASS')

def main():
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest='cmd',required=True)
    g=sp.add_parser('generate');g.add_argument('--seed',required=True);g.add_argument('--role',choices=['CAL','TRAIN','TEST','DEV'],required=True);g.add_argument('--count',type=int,required=True);g.add_argument('--out',required=True)
    c=sp.add_parser('calibrate');c.add_argument('--manifest',required=True);c.add_argument('--out',required=True)
    sp.add_parser('selftest');a=ap.parse_args()
    if a.cmd=='selftest':selftest();return
    if a.cmd=='generate':
        S=suite(bytes.fromhex(a.seed),a.role,a.count);json.dump({'role':a.role,'instances':[enc(x) for x in S]},open(a.out,'w'),indent=2,sort_keys=True);open(a.out,'a').write('\n')
    else:
        raw=open(a.manifest,'rb').read();d=json.loads(raw);z=calibrate([dec(x) for x in d['instances']]);z['manifest_sha256']=sha256(raw).hexdigest();json.dump(z,open(a.out,'w'),indent=2,sort_keys=True);open(a.out,'a').write('\n')
if __name__=='__main__':main()
