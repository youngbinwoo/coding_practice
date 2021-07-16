n=int(input())
num=list(map(int,input().split()))
dp=[0]*n
dp[0]=num[0]

for i in range(1,len(num)):
    if num[i]>dp[i-1]+num[i]:
        dp[i]=num[i]
    else:
        dp[i]=dp[i-1]+num[i]

print(max(dp))
