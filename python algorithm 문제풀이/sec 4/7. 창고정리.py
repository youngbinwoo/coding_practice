import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
num=list(map(int, input().split()))
m=int(input())

a=0
b=0
for _ in range(m):
    ma=0
    mi=100
    for i in range(n):
        if num[i]>ma:
            ma=num[i]
            a=i
    for j in range(n):
        if num[j]<mi:
            mi=num[j]
            b=j
    num[a]=num[a]-1
    num[b]=num[b]+1


print(max(num)-min(num))
