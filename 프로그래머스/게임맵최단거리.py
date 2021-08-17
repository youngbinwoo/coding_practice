from collections import deque
def bfs(x,y,maps):
    q=deque()
    n=len(maps[0])
    m=len(maps)
    D=[[0]*n for _ in range(m)]
    D[x][y]=1
    q.append((x,y))
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    while q:
        x,y=q.popleft()
        if x==len(maps) and y==len(maps[0]):
            break
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<len(maps) and 0<=yy<len(maps[0]) and maps[xx][yy]==1 and D[xx][yy]==0:
                D[xx][yy]=D[x][y]+1
                q.append((xx,yy))
    
    return D[m-1][n-1]

def solution(maps):
    if bfs(0,0,maps)==0:
        return -1
    else:
        return bfs(0,0,maps)
