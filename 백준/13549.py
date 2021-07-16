import sys
from collections import deque
sys.setrecursionlimit(10**6)
a,b=map(int,input().split())
Max=100000
ch=[0]*Max
ch[a]=1

q=deque()
q.append(a)
while q:
    m=q.popleft()
    if m==b:
        print(ch[b]-1)
        break
    if m*2<Max and ch[m*2]==0:
        q.appendleft(m*2)
        ch[m*2]=ch[m]
    if 0<=m-1<Max and ch[m-1]==0:
        q.append(m-1)
        ch[m-1]=ch[m]+1
    if m+1<Max and ch[m+1]==0:
        ch[m+1]=ch[m]+1
        q.append(m+1)
