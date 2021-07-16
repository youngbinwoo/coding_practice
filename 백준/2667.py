import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    global cnt
    if ch[x][y]==1:
        return 
    ch[x][y]=1

    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n:
            if ch[xx][yy]==0 and num[xx][yy]==1:
                cnt+=1
                dfs(xx,yy)

if __name__=="__main__":
    n=int(input())
    num=[]
    ch=[[0]*n for _ in range(n)]
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    for _ in range(n):
        num.append(list(map(int,input())))

    ans=[]
    for i in range(n):
        for j in range(n):
            if ch[i][j]==0 and num[i][j]==1:
                cnt=1
                dfs(i,j)
                ans.append(cnt)

    print(len(ans))
    ans.sort()
    for z in ans:
        print(z)
