import sys
sys.stdin=open("input.txt", "r")
def DFS(x):
    global cnt 
    if x==m:
        cnt+=1
        for i in range(len(res)):
            print(res[i],end=' ')
        print()
    else:
        for i in range(1,n+1):
            res[x]=i
            DFS(x+1)

if __name__=="__main__":
    n,m=map(int,input().split())
    res=[0]*m
    cnt=0
    DFS(0)
    print(cnt)
