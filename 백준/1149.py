n=int(input())
num=list(list(map(int,input().split())) for _ in range(n))
dp=[[0]*len(num[0]) for _ in range(n)]
dp[0][0]=num[0][0]
dp[0][1]=num[0][1]
dp[0][2]=num[0][2]

for i in range(1,n):
    for j in range(len(num[0])):
        if j==0:
            dp[i][j]=num[i][j]+min(dp[i-1][j+1],dp[i-1][j+2])
        elif j==1:
            dp[i][j]=num[i][j]+min(dp[i-1][j-1],dp[i-1][j+1])
        elif j==2:
            dp[i][j]=num[i][j]+min(dp[i-1][j-2],dp[i-1][j-1])
print(min(dp[n-1]))
