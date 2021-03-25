import sys
sys.stdin=open("input.txt", "r")

def DFS(x,L):
    global cnt
    if x==b:
        for j in p:
            print(j,end=' ')
        print()
        cnt+=1
    else:
        for i in range(L,a+1):
            p[x]=i
            DFS(x+1,p[x]+1)



if __name__=="__main__":
    a,b=map(int,input().split())
    p=[0]*b
    cnt=0
    DFS(0,1)
    print(cnt)
