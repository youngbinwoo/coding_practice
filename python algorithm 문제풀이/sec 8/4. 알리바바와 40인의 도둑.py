import sys
#sys.stdin=open("input.txt", "r")

def DFS(x,y):
    if dp[x][y]>0:
        return dp[x][y]
    if x==0 and y==0:
        return L[0][0]
    else:
        if x==0:
            dp[x][y]=DFS(x,y-1)+L[x][y]
        if y==0:
            dp[x][y]=DFS(x-1,y)+L[x][y]
        else:
            dp[x][y]=min(DFS(x,y-1),DFS(x-1,y))+L[x][y]
    return dp[x][y]


if __name__=="__main__":
    n=int(input())
    L=[list(map(int,input().split())) for _ in range(n)]
    dp=[[0]*n for _ in range(n)]
    print(DFS(n-1,n-1))