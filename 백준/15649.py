def DFS(L):
    if L==b:
        for i in range(len(res)):
            print(res[i],end=' ')
        print()
    else:
        for i in range(len(num)):
            if ch[i]==0:
                ch[i]=1
                res[L]=num[i]
                DFS(L+1)
                ch[i]=0

if __name__=="__main__":
    a,b=map(int,input().split())
    num=[i for i in range(1,a+1)]
    res=[0]*b
    ch=[0]*a
    DFS(0)
