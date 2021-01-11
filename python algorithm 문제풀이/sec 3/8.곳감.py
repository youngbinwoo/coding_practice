import sys
sys.stdin=open("input.txt", "rt")
n=int(input())
lis=[list(map(int,input().split())) for _ in range(n)]
num=int(input())

for i in range(num):
    a,b,c=map(int,input().split())
    if b==0:
        for i in range(c):
            lis[a-1].append(lis[a-1].pop(0))
    else:
        for i in range(c):
            lis[a-1].insert(0,lis[a-1].pop())


e=0
s=n
res=0
em=n//2
for i in range(n):
    for j in range(e,s):
        res+=lis[i][j]
    if i >=em:
        e-=1
        s+=1
    else:
        e+=1
        s-=1
print(res)
