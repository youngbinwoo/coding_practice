n=int(input())
num=list(map(int,input().split()))
num.insert(0,0)
dp=[0]*(n+1)
dp[1]=num[1]


for j in range(2,n+1):
    dp[j]=num[j]
    for i in range(1,j):
        if i==1:
           dp[j]=max(dp[0]*(j),dp[j])

        dp[j]=max(dp[j-i]+dp[i],dp[j])

print(dp[n])
