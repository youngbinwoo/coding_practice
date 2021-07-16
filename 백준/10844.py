n=int(input())
mod=1000000000
dp=[[0]*10 for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(10):
        if i==1:
            if j==0:
                dp[i][j]=0
            else:
                dp[i][j]=1
        else:
            if j==0:
                dp[i][j]=dp[i-1][j+1]
            elif j==9:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]+=dp[i-1][j-1]
                dp[i][j]+=dp[i-1][j+1]

print(sum(dp[n])%mod)
