import sys
sys.stdin=open("input.txt", "r")

def DFS(T,M):
    global res
    if T==n+1:
        if M>res:
            res=M
    else:
        if T+pt[T]<=n+1:
            DFS(T+pt[T],M+pv[T])
        DFS(T+1,M)

if __name__=="__main__":
    n=int(input())
    pt=list()
    pv=list()
    for i in range(n):
        a, b=map(int, input().split())
        pt.append(a)
        pv.append(b)
    pt.insert(0,0)
    pv.insert(0,0)
    res=-123
    DFS(1,0)
    print(res)
