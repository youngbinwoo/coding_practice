def DFS(L):
    global res,aa
    if L==n:
        s=0
        i=0
        j=1
        while j!=n:
            if num[ans[i]-1][ans[j]-1]==0 or num[ans[-1]-1][ans[0]-1]==0:
                s=0
                break
            else:
                s+=num[ans[i]-1][ans[j]-1]
                j+=1
                i+=1
        if s!=0:
            res=min(s+num[ans[-1]-1][ans[0]-1],res)
    else:
        for i in range(1,len(ans)):
            if ch[i]==0:
                aa=lis[i]-1
                ch[i]=1
                ans[L]=lis[i]
                DFS(L+1)
                ch[i]=0

n=int(input())
res=12340000000000
aa=0
num=list(list(map(int,input().split())) for _ in range(n))
lis=[i for i in range(1,n+1)]
ans=[0]*n
ans[0]=1
ch=[0]*n
DFS(1)
print(res)
