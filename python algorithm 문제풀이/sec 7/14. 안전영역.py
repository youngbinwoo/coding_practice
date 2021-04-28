import sys
from collections import deque
sys.stdin=open("input.txt", "r")

n=int(input())
num=[list(map(int,input().split())) for _ in range(n)]
h=-1
q=deque()
dx=[-1,0,1,0]
dy=[0,-1,0,1]
res=[]

for i in range(len(num)):
    if max(num[i])>h:
        h=max(num[i])

for H in range(1,h):
    cnt=0
    c=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if num[i][j]>H and c[i][j]==0:
                c[i][j]=1
                cnt+=1
                q.append((i,j))
                while q:
                    now=q.popleft()
                    for z in range(4):
                        xx=now[0]+dx[z]
                        yy=now[1]+dy[z]
                        if 0<=xx<n and 0<=yy<n and num[xx][yy]>H and c[xx][yy]==0:
                            c[xx][yy]=1
                            q.append((xx,yy))
    res.append(cnt)

print(max(res))
