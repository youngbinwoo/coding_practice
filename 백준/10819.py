def DFS(L):
    global s
    if L==n:
        i=0
        j=1
        res=0
        while j!=n:
            res+=abs(ans[i]-ans[j])
            i+=1
            j+=1
        s=max(res,s)
    else:
        for i in range(len(num)):
            if ch[i]==0:
                ch[i]=1
                ans[L]=num[i]
                DFS(L+1)
                ch[i]=0

n=int(input())
num=list(map(int,input().split()))
ch=[0]*n
ans=[0]*n
s=0
DFS(0)
print(s)
