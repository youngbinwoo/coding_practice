import sys
from collections import deque

n,m=map(int,input().split())
num=list(list(map(int,input().split())) for _ in range(m))
ch=[[0]*n for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()


for i in range(m):
    for j in range(n):
        if num[i][j]==1 and ch[i][j]==0:
            q.append((i,j))
while q:
    a,b=q.popleft()
    for i in range(4):
        xx=a+dx[i]
        yy=b+dy[i]
        if 0<=xx<m and 0<=yy<n:
            if num[xx][yy]==0 and ch[xx][yy]==0:
                num[xx][yy]=1
                ch[xx][yy]=ch[a][b]+1
                q.append((xx,yy))

f=0
Max=0
for i in range(m):
    for j in range(n):
        if num[i][j]==0:
            f=1
            break
    Max=max(Max,max(ch[i]))

if f==1:
    print(-1)
else:
    print(Max)
