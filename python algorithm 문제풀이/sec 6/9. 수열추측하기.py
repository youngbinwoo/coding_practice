import sys
sys.stdin=open("input.txt", "r")
def DFS(x,s):
    if x==a and s==b:
        for j in p:
            print(j, end=' ')
        sys.exit(0)
    else:
        for i in range(1,a+1):
            if ch[i]==0:
                ch[i]=1
                p[x]=i
                DFS(x+1,s+(p[x]*c[x]))
                ch[i]=0

if __name__=="__main__":
    a,b=map(int,input().split())
    ch=[0]*(a+1)
    c=[1]*a
    p=[0]*(a)
    for i in range(1,a):
        c[i]=c[i-1]*(a-i)//i
    DFS(0,0)
