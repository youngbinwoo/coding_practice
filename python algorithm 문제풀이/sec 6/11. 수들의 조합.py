import sys
sys.stdin=open("input.txt", "r")

def DFS(x,L,s):
    global cnt
    if x==b:
        if s%c==0:
            cnt+=1
    else:
        for i in range(L,a+1):
            p[x]=l[i-1]
            DFS(x+1,i+1,s+p[x])



if __name__=="__main__":
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    c=int(input())
    p=[0]*(b)
    cnt=0
    DFS(0,1,0)
    print(cnt)
