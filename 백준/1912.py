n=int(input())
num=list(map(int,input().split()))
num.insert(0,0)
dp=[[0]*(n+1) for _ in range(n+1)]
m=-1001

for i in range(n+1):
    for j in range(i+1,n+1):
        if i==0:
            dp[i][j]=num[j]
            if dp[i][j]>m:
                m=dp[i][j]

        else:
            dp[i][j]=num[j]+dp[i-1][j-1]
            if dp[i][j]>m:
                m=dp[i][j]

print(m)
