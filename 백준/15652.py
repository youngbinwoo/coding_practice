def DFS(L):
    global aa
    if L==b:
        for i in range(len(res)):
            print(res[i],end=' ')
        print()


    else:
        for i in range(len(num)):
            if aa<=num[i]:
                aa=num[i]
                res[L]=num[i]
                DFS(L+1)
                aa=0

if __name__=="__main__":
    aa=0
    a,b=map(int,input().split())
    num=[i for i in range(1,a+1)]
    res=[0]*b
    DFS(0)
