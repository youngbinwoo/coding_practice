n=int(input())
num=list(map(int,input().split()))
num.insert(0,12345678910)
dp=[0]*(n+1)
dp[0]=num[0]
dp[1]=num[1]


for j in range(2,n+1):
    dp[j]=num[j]
    for i in range(1,j):
        if i==1:
           dp[j]=min(dp[0]*(j),dp[j])

        dp[j]=min(dp[j-i]+dp[i],dp[j])

print(dp[n])
