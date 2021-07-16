def DFS(L,S):
    global res
    if L==n:
        res=max(res,S)
    else:
        if L+T[L]<=n:
            DFS(L+T[L],S+M[L])
        DFS(L+1,S)


if __name__=="__main__":
    n=int(input())
    T=[]
    M=[]
    for i in range(n):
        a,b=map(int,input().split())
        T.append(a)
        M.append(b)
    res=0
    DFS(0,0)
    print(res)
