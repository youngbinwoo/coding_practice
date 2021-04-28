import sys
from collections import deque
sys.stdin=open("input.txt", "r")

n=int(input())
num=[list(map(int,input())) for _ in range(n)]
res=[]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
q=deque()

for i in range(n):
    for j in range(n):
        if num[i][j]==1:
            cnt=0
            q.append((i,j))
            while q:
                now=q.popleft()
                for j in range(4):
                    xx=now[0]+dx[j]
                    yy=now[1]+dy[j]
                    if 0<=xx<n and 0<=yy<n:
                        if num[xx][yy]==1:
                            cnt+=1
                            num[xx][yy]=0
                            q.append((xx,yy))
            if cnt==0:
                res.append(1)
            else:
                res.append(cnt)

print(len(res))
res.sort()
for i in res:
    print(i)
