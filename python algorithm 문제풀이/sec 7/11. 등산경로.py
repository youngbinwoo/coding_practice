import sys
sys.stdin=open("input.txt", "r")

def DFS(x,y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for j in range(4):
            xx=x+dx[j]
            yy=y+dy[j]
            if 0<=xx<n and 0<=yy<n:
                if num[xx][yy]>num[x][y]:
                    DFS(xx,yy)

if __name__=="__main__":
    n=int(input())
    num=[list(map(int,input().split())) for _ in range(n)]
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    max=-2147000000
    min=2147000000
    sx=0
    sy=0
    ex=0
    ey=0
    cnt=0
    for i in range(n):
        for j in range(n):
            if num[i][j]>max:
                max=num[i][j]
                ex=i
                ey=j
            if num[i][j]<min:
                min=num[i][j]
                sx=i
                sy=j
    DFS(sx,sy)
    print(cnt)
