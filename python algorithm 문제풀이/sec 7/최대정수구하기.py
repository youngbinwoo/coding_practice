import sys
#sys.stdin=open("input.txt", "r")
def DFS(L,x,s):
    global me
    if s>m or L==n:
        return
    if s==m:
        if x>me:
            me=x
    else:
        for i in range(n):
            if ch[L]==0:
                ch[L]=1
                DFS(L+1,x+sI[i],s+mI[i])
                ch[L]=0


if __name__=="__main__":
    n, m=map(int, input().split())
    sI=[]
    mI=[]
    for i in range(n):
        a, b=map(int, input().split())
        sI.append(a)
        mI.append(b)
    me=-100
    ch=[0]*(n+1)
    DFS(0,0,0)
    print(me)