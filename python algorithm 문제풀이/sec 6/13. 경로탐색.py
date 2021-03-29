import sys
sys.stdin=open("input.txt", "r")

def DFS(x):
    global cnt
    if x==n:
        cnt+=1
    else:
        for i in range(n+1):
            if ch[i]==0 and g[x][i]==1:
                ch[i]=1
                DFS(i)
                ch[i]=0


if __name__=="__main__":
    n,m=map(int,input().split())
    g=[[0]*(n+1) for _ in range(n+1)]
    for i in range(m):
        a,b= map(int,input().split())
        g[a][b]=1
    ch=[0]*(n+1)
    cnt=0
    ch[1]=1
    DFS(1)
    print(cnt)
