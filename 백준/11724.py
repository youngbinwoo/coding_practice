import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    if ch[x]==1:
        return
    ch[x]=1

    for y in num[x]:
        if ch[y]==0:
            dfs(y)

if __name__=="__main__":
    n,m=map(int,sys.stdin.readline().split())
    ch=[0]*(n+1)
    num=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b=map(int,sys.stdin.readline().split())
        num[a].append(b)
        num[b].append(a)

    cnt=0
    for i in range(1,n+1):
        if ch[i]==0:
            dfs(i)
            cnt+=1 
print(cnt)
