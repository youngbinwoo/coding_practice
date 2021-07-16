import sys
from collections import deque
sys.setrecursionlimit(10**6)
a,b=map(int,input().split())
ch=[0]*100001

q=deque()
q.append(a)
while q:
    m=q.popleft()
    if m==b:
        print(ch[b])
        break
    xx=m+1
    yy=m-1
    zz=m*2
    if 0<=xx<100001:
        if ch[xx]==0:
            ch[xx]=ch[m]+1
            q.append(xx)
    if 0<=yy<100001:
        if ch[yy]==0:
            ch[yy]=ch[m]+1
            q.append(yy)
    if 0<=zz<100001:
        if ch[zz]==0:
            ch[zz]=ch[m]+1
            q.append(zz)
