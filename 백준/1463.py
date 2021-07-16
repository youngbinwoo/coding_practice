n=int(input())
dp=[0]*(n+1)
dp[0]=0
dp[1]=1
dp[2]=1

for i in range(3,n):
    dp[i]=dp[(i+1)-2]+1
    if (i+1)%2==0 and dp[i]>dp[(i+1)//2-1]+1:
        dp[i]=dp[(i+1)//2-1]+1
    if (i+1)%3==0 and dp[i]>dp[(i+1)//3-1]+1:
        dp[i]=dp[(i+1)//3-1]+1

print(dp[n-1])
