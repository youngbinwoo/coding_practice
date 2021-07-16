n=int(input())
mod=9901
D=[[0]*3 for i in range(n+1)]
D[1][0]=D[1][1]=D[1][2]=1

for N in range(2,n+1):
    D[N][0]=D[N-1][0]+D[N-1][1]+D[N-1][2]
    D[N][1]=D[N-1][0]+D[N-1][2]
    D[N][2]=D[N-1][0]+D[N-1][1]

    D[N][0]%=mod
    D[N][1]%=mod
    D[N][2]%=mod

print(sum(D[n])%mod)
