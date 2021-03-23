import sys
sys.stdin=open("input.txt", "r")
def DFS(x,s):
    global res
    if x>res:
        return
    if s>m:
        return
    if s==m:
        if x <res:
            res=x
    else:
        for i in range(n):
            DFS(x+1,s+c[i])

if __name__=="__main__":
    n=int(input())
    c=list(map(int,input().split()))
    m=int(input())
    res=10000000000
    c.sort(reverse=True)
    DFS(0,0)
    print(res)
