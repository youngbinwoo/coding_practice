def DFS(s):
    global cnt
    if s==m:
        cnt+=1
    if s>m:
        return
    else:
        for i in range(len(num)):
            DFS(s+num[i])


if __name__=="__main__":
    num=[1,2,3]
    n=int(input())
    for i in range(n):
        cnt=0
        m=int(input())
        DFS(0)
        print(cnt)
