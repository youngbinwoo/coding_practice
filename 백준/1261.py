from collections import deque
n,m=map(int,input().split())
num=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
ch=[[0]*n for _ in range(m)]
for _ in range(m):
    num.append(list(map(int,input())))

q=deque()
q.append((0,0))
ch[0][0]=1
while q:
    x,y=q.popleft()
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<m and 0<=yy<n and ch[xx][yy]==0:
            if num[xx][yy]==0:
                q.appendleft((xx,yy))
                ch[xx][yy]=ch[x][y]
            if num[xx][yy]==1:
                q.append((xx,yy))
                ch[xx][yy]=ch[x][y]+1
print(ch[m-1][n-1]-1)
print(ch)
