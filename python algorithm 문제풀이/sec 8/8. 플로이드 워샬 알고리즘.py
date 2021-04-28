import sys
#sys.stdin=open("input.txt", "r")
n,m=map(int,input().split())
dis=list([5000]*(n) for _ in range(n))


for _ in range(m):
    a,b,c=map(int,input().split())
    dis[a-1][b-1]=c

for i in range(n):
    dis[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])

 
for i in range(n):
    for j in range(n):
        if dis[i][j]==5000:
            print("M",end=' ')
        else:
            print(dis[i][j],end=' ')
    print()