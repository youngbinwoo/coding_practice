import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
dis=list([5000]*(n) for _ in range(n))
f=[0]*n

while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    else: 
        dis[a-1][b-1]=1
        dis[b-1][a-1]=1

for i in range(n):
    dis[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])
            dis[j][i]=min(dis[i][j],dis[i][k]+dis[k][j])

for i in range(n):
    M=-1
    for j in range(n):
        if dis[i][j]>M:
            M=dis[i][j]
    f[i]=M

cnt=0
ans=[]
for i in range(n):
    if f[i]==min(f):
        cnt+=1
        ans.append(i+1)
print(min(f), cnt)
for i in range(len(ans)):
    print(ans[i],end=' ')
