import sys
sys.stdin=open("input.txt", "rt")
n=int(input())
lis=[list(map(int,input().split())) for _ in range(n)]

en=len(lis[0])
lis.insert(0,[0]*(n+2))
lis.append([0]*(n+2))
cnt=0

for i in range(1,n+1):
    lis[i].insert(0,0)
    lis[i].append(0)

for i in range(1,n+1):
    for j in range(1,n+1):
        if lis[i][j]>lis[i-1][j] and lis[i][j]>lis[i][j-1] and  lis[i][j]>lis[i+1][j] and lis[i][j]>lis[i][j+1]:
            cnt+=1


print(cnt)
