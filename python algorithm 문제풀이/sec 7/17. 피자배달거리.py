import sys
sys.stdin=open("input.txt", "r")

def DFS(L,x):
    global dis,sum
    if L==m:
        sum=0
        for j in range(len(h)):
            x1=h[j][0]
            y1=h[j][1]
            dis=214700000
            for z in range(len(res)):
                x2=res[z][0]
                y2=res[z][1]
                dis=min(dis,abs(x1-x2)+abs(y1-y2))
            sum+=dis
        ans.append(sum)
    else:
        for i in range(x,len(piz)):
            res[L]=piz[i]
            DFS(L+1,i+1)
            res[L]=0


if __name__=="__main__":
    piz=[]
    h=[]
    n,m=map(int,input().split())
    res=[0]*m
    num=[list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if num[i][j]==2:
                piz.append((i,j))
            elif num[i][j]==1:
                h.append((i,j))
    ans=[]
    DFS(0,0)
    print(min(ans))
