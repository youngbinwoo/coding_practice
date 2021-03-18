import sys
sys.stdin=open("input.txt", "r")


def DFS(x,y):
    global swich
    s=0
    if x==n:
        for i in range(n):
            if chr[i]==1:
                s+=num[i]
        if s==total-s:
            swich=1
    else:
        chr[y]=1
        DFS(x+1,y+1)
        chr[y]=0
        DFS(x+1,y+1)

if __name__=="__main__":
    swich=0
    n=int(input())
    chr=[0]*(n+1)
    num=list(map(int,input().split()))
    total=sum(num)
    DFS(0,0)
    if swich==0: print("NO")
    else: print("YES")
