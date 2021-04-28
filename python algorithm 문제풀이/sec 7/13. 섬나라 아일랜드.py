import sys
from collections import deque
sys.stdin=open("input.txt", "r")

def DFS(x,y):
    global cnt
    cnt+=1
    num[x][y]=0
    for j in range(8):
        xx=x+dx[j]
        yy=y+dy[j]
        if 0<=xx<n and 0<=yy<n and num[xx][yy]==1:
            DFS(xx,yy)

if __name__=="__main__":
    n=int(input())
    num=[list(map(int,input().split())) for _ in range(n)]
    res=[]
    cnt=0
    dx=[-1, -1, -1, 0, 1, 0,1,1]
    dy=[-1, 0, 1, 1, 0, -1,1,-1]
    for i in range(n):
        for j in range(n):
            if num[i][j]==1:
                DFS(i,j)
                res.append(cnt)
print(len(res))
