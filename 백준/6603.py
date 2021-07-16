def DFS(L):
    global aa
    if L==6:
        for i in range(len(ans)):
            print(ans[i], end=' ')
        print()
    
    else:
        for i in range(len(r)):
            if ch[i]==0 and aa<r[i]:
                ch[i]=1
                aa=r[i]
                ans[L]=r[i]
                DFS(L+1)
                ch[i]=0
                aa=0


while True:
    r=list(map(int,input().split()))
    n=r.pop(0)
    if len(r)==0 and n==0:
        break
    aa=-1
    ans=[0]*6
    ch=[0]*len(r)
    DFS(0)
    print()
