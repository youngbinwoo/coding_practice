n=int(input())
num=list(map(int,input().split()))
dp=[0]*n
dp[0]=1

for i in range(1,n):
    aa=0
    for j in range(i):
        if num[i]>num[j]:
            if aa<dp[j]:
                aa=dp[j]
    dp[i]=aa+1

print(max(dp))
