import sys
from collections import deque
sys.setrecursionlimit(10**6)
n=int(input())
dx=[2,1,-1,-2,-2,-1,1,2]
dy=[1,2,2,1,-1,-2,-2,-1]
for _ in range(n):
    m=int(input())
    s1,s2=map(int,input().split())
    e1,e2=map(int,input().split())
    ch=[[0]*m for _ in range(m)]

    q=deque()
    q.append((s1,s2))
    while q:
        a,b=q.popleft()
        if a==e1 and b==e2:
            print(ch[e1][e2])
            break
        for i in range(8):
            xx=dx[i]+a
            yy=dy[i]+b
            if 0<=xx<m and 0<=yy<m:
                if ch[xx][yy]==0:
                    ch[xx][yy]=ch[a][b]+1
                    q.append((xx,yy))
