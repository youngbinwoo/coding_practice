def dfs(L,sum):
    global cnt
    if L>=n:
        return
    if sum+a[L]==s:
        cnt+=1
    dfs(L+1,sum)
    dfs(L+1,sum+a[L])

n,s=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
dfs(0,0)
print(cnt)
