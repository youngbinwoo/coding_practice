a,b=map(int,input().split())
D=[[0]*(b+1) for _ in range(a+1)]
mod=1000000000
for i in range(a+1):
    for j in range(1,b+1):
        if j==1:
            D[i][j]=1
        else:
            for k in range(i+1):
                D[i][j]+=D[k][j-1]
                D[i][j]%=mod

print(D[a][b]%mod)
