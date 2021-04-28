import sys
sys.stdin=open("input.txt", "r")

def DFS(L,a,b,c):
    global res
    if L==n:
        if a!=b and b!=c and a!=c:
            lis=[a,b,c]
            if max(lis)-min(lis)<res:
                res=max(lis)-min(lis)

    else:
        DFS(L+1,a+num[L],b,c)
        DFS(L+1,a,b+num[L],c)
        DFS(L+1,a,b,c+num[L])

if __name__=="__main__":
    n=int(input())
    num=[]
    res=999
    for i in range(n):
        a=int(input())
        num.append(a)
    DFS(0,0,0,0)
    print(res)
