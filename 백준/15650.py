def DFS(L):
    global aa
    if L==b:
        for i in range(len(res)):
            print(res[i],end=' ')
        print()


    else:
        for i in range(len(num)):
            if ch[i]==0 and aa<num[i]:
                aa=num[i]
                ch[i]=1
                res[L]=num[i]
                DFS(L+1)
                ch[i]=0
                aa=0


if __name__=="__main__":
    a,b=map(int,input().split())
    aa=0
    num=[i for i in range(1,a+1)]
    res=[0]*b
    ch=[0]*a
    DFS(0)
