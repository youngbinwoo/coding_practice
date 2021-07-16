n=int(input())
num=[]
for _ in range(n):
    num.append(int(input()))

D=[[0]*3 for _ in range(n)]
D[0][1]=num[0]

for i in range(1,n):
    D[i][0]=max(D[i-1][0],D[i-1][1],D[i-1][2])
    D[i][1]=D[i-1][0]+num[i]
    D[i][2]=D[i-1][1]+num[i]

print(max(D[n-1]))
