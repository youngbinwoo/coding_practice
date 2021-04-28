import sys
from collections import deque
sys.stdin=open("input.txt", "r")

dx=[-1,0,+1,0]
dy=[0,1,0,-1]
q=deque()
cnt=0
num=[list(map(int,input().split())) for I in range(7)]
q.append((0,0))

dis=[[0]*7 for _ in range(7)]
num[0][0]=1

while q:
    a=len(q)
    for _ in range(a):
        now=q.popleft()
        for j in range(4):
            x=now[0]+dx[j]
            y=now[1]+dy[j]
            if 0<=x<=6 and 0<=y<=6:
                if num[x][y]==0:
                    dis[x][y]+=dis[now[0]][now[1]]+1
                    q.append((x,y))
                    num[x][y]=1
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])
