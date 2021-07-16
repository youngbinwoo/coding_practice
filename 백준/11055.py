n=int(input())
num=list(map(int,input().split()))
dp=[0]*n
dp[0]=num[0]

for i in range(1,n):
    for j in range(i):
        if num[i]>num[j]:
            dp[i]=max(dp[i],num[i]+dp[j])
    if dp[i]==0:
        dp[i]=num[i]

print(max(dp))
