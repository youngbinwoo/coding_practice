n=int(input())
num=list(map(int,input().split()))
dp=[0]*n
dv=[0]*n
dp[0]=1

for i in range(1,n):
    aa=0
    bb=0
    for j in range(i):
        if num[i]>num[j]:
            if aa<=dp[j]:
                aa=dp[j]
                dv[i]=j+1
    dp[i]=aa+1
    dv[i]==bb

m=0
x=0
for i in range(len(dp)):
    if dp[i]>m:
        m=dp[i]
        x=i
ans=[]
for i in range(m):
    ans.append(num[x])
    x=dv[x]-1

ans.reverse()
print(m)
print(' '.join(map(str,ans)))
