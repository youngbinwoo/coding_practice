import sys
from collections import deque
sys.stdin=open("input.txt", "r")

dx=[-1,0,1,0]
dy=[0,-1,0,1]
q=deque()
n,m=map(int,input().split())
num=[list(map(int,input().split())) for _ in range(m)]
ch=[[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if num[i][j]==1 and ch[i][j]==0:
            q.append((i,j))

while q:
    now=q.popleft()
    for j in range(4):
        xx=now[0]+dx[j]
        yy=now[1]+dy[j]
        if 0<=xx<m and 0<=yy<n:
            if num[xx][yy]==0 and ch[xx][yy]==0:
                num[xx][yy]=1
                ch[xx][yy]=ch[now[0]][now[1]]+1
                q.append((xx,yy))

max=-111
f=0
for i in range(m):
    for j in range(n):
        if num[i][j]==0:
            f=1
            
if f==0:
    for i in range(m):
        for j in range(n):
            if ch[i][j]>max:
                max=ch[i][j]
    print(max)
else:
    print(-1)
