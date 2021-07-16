n=int(input())
num=list(map(int,input().split()))

dp=[[0]*2 for i in range(n)]
dp[0][0]=num[0]
dp[0][1]=0

m=num[0]
for i in range(1,n):
    dp[i][0]=max(num[i],dp[i-1][0]+num[i])
    dp[i][1]=max(dp[i-1][0],dp[i-1][1]+num[i])
    m=max(m,dp[i][0],dp[i][1])

print(m)
