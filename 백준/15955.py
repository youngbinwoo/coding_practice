def DFS(L):
    global aa
    if L==b:
        for i in range(len(res)):
            print(res[i],end=' ')
        print()


    else:
        for i in range(len(num)):
            if ch[i]==0 and aa<num[i]:
                ch[i]=1
                aa=num[i]
                res[L]=num[i]
                DFS(L+1)
                ch[i]=0
                aa=0

if __name__=="__main__":
    aa=0
    a,b=map(int,input().split())
    num=list(map(int,input().split()))
    num.sort()
    ch=[0]*a
    res=[0]*b
    DFS(0)
