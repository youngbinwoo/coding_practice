n=int(input())
num=[]
for _ in range(n):
    num.append(list(map(int,input().split())))

dp=[[0]*n for _ in range(n)]
dp[0][0]=num[0][0]


for i in range(n-1):
    for j in range(len(num[i])):
        dp[i+1][j]=max(dp[i+1][j],num[i+1][j]+dp[i][j])
        dp[i+1][j+1]=max(dp[i+1][j+1],num[i+1][j+1]+dp[i][j])

print(max(dp[n-1]))
