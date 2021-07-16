import sys
sys.setrecursionlimit(10**6)
from collections import deque

def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
        a,b=q.popleft()
        for i in range(4):
            xx=dx[i]+a
            yy=dy[i]+b
            if 0<=xx<m and 0<=yy<n:
                if num[xx][yy]==0 and r_ch[xx][yy]==0:
                    r_ch[xx][yy]=1
                    ch[xx][yy]=min(ch[xx][yy],ch[a][b]+1)
                    q.append((xx,yy))


if __name__=="__main__":
    n,m=map(int,input().split())
    num=[]
    r=10000
    ch=[[r]*n for _ in range(m)]
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    for _ in range(m):
        num.append(list(map(int,input().split())))

    for i in range(m):
        for j in range(n):
            if num[i][j]==1:
                ch[i][j]=0
                r_ch=[[0]*n for _ in range(m)]
                r_ch[i][j]=1
                bfs(i,j)
            if num[i][j]==-1:
                ch[i][j]=-1
    
    Max=0
    for z in range(m):
        Max=max(Max,max(ch[z]))
    
    if Max==r:
        print(-1)
    else:
        print(Max)
