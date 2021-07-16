def DFS(L):
    global aa
    if L==b:
        for i in range(len(res)):
            print(res[i],end=' ')
        print()


    else:
        for i in range(len(num)):
            res[L]=num[i]
            DFS(L+1)

if __name__=="__main__":
    a,b=map(int,input().split())
    num=list(map(int,input().split()))
    num.sort()
    res=[0]*b
    DFS(0)
