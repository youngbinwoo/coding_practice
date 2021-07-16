import sys
from collections import deque
sys.setrecursionlimit(10**6)
def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        a,b=q.popleft()
        for i in range(4):
            xx=a+dx[i]
            yy=b+dy[i]
            if 0<=xx<n and 0<=yy<m:
                if num[xx][yy]==1:
                    num[xx][yy]=0
                    ch[xx][yy]=ch[a][b]+1
                    q.append((xx,yy))


if __name__=="__main__":
    n,m=map(int,sys.stdin.readline().split())
    num=[]
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    ch=[[0]*m for _ in range(n)]
    for _ in range(n):
        num.append(list(map(int,input())))

    num[0][0]=0
    ch[0][0]=1
    bfs(0,0)
    print(ch[n-1][m-1])
