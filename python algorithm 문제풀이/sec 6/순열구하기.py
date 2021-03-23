import sys
sys.stdin=open("input.txt", "r")
def DFS(x):
    global cnt
    if x==b:
        for i in range(len(res)):
            if res[i]!=0:
                print(res[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,a+1):
            if ch[i]==0:
                res[x]=i
                ch[i]=1
                DFS(x+1)
                ch[i]=0


if __name__=="__main__":
    a,b=map(int,input().split())
    cnt=0
    res=[0]*(a+1)
    ch=[0]*(a+1)
    DFS(0)
    print(cnt)
