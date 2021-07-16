n=int(input())
dp=[0]*(1000001)
mod=1000000009
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(4,1000001):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    dp[i]%=mod

for _ in range(n):
    m=int(input())
    print(dp[m]%mod)
