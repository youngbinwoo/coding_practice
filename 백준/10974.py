def DFS(L):
    if L==n:
        print(' '.join(map(str,ans)))
    for i in range(n):
        if ch[i]==0:
            ch[i]=1
            ans[L]=i+1
            DFS(L+1)
            ch[i]=0
           
n=int(input())
ch=[0]*n
ans=[0]*n
DFS(0)
