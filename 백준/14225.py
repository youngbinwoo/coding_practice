def dfs(L,s):
    ch[s]=1
    if L>=n:
        return
    else:
        dfs(L+1,s)
        dfs(L+1,s+num[L])

if __name__=="__main__":
    n=int(input())
    num=list(map(int,input().split()))
    ch=[0]*(sum(num)+2)
    dfs(0,0)
    for i in range(1,len(ch)):
        if ch[i]!=1:
            print(i)
            break
