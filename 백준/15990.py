# D[i][j] : i를 1,2,3 을 사용하여 나타낸 방법 수 (j는 마지막으로 사용한 수)
s=1000000009

D=[[0]*4 for i in range(100001)]
D[1][1]=1
D[2][2]=1
D[3][1]=1
D[3][2]=1
D[3][3]=1

n=int(input())
for m in range(4,100001):
    D[m][1]=D[m-1][2]+D[m-1][3]
    D[m][2]=D[m-2][1]+D[m-2][3]
    D[m][3]=D[m-3][1]+D[m-3][2]
    
    D[m][1]%=s
    D[m][2]%=s
    D[m][3]%=s

for _ in range(n):
    k=int(input())
    print(sum(D[k])%s)
