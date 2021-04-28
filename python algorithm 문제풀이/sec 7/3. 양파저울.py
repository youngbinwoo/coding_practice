import sys
sys.stdin=open("input.txt", "r")

def DFS(l,s):
    global cnt, res
    if l==n or s==S:
        if s>0:
            res.append(s)

    else:
        if s>0:
            res.append(s)
        DFS(l+1,s+num[l])
        DFS(l+1,s-num[l])
        DFS(l+1,s)

if __name__=="__main__":
    n=int(input())
    num=list(map(int,input().split()))
    S=sum(num)
    cnt=0
    res=list()
    DFS(0,0)
    res=list(set(res))
    print(S-len(res))
