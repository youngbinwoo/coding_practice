import sys
from collections import deque
sys.setrecursionlimit(10**6)
a,b=map(int,input().split())
ch=[0]*100001
f=[0]*100001

q=deque()
q.append(a)
while q:
    m=q.popleft()
    if m==b:
        print(ch[b])
        res=[b]
        while b!=a:
            res.append(f[b])
            b=f[b]
        break
    xx=m+1
    yy=m-1
    zz=m*2
    if 0<=xx<100001:
        if ch[xx]==0:
            ch[xx]=ch[m]+1
            f[xx]=m
            q.append(xx)
    if 0<=yy<100001:
        if ch[yy]==0:
            ch[yy]=ch[m]+1
            f[yy]=m
            q.append(yy)
    if 0<=zz<100001:
        if ch[zz]==0:
            ch[zz]=ch[m]+1
            f[zz]=m
            q.append(zz)

for i in range(1,len(res)+1):
    print(res[-i],end=' ')
