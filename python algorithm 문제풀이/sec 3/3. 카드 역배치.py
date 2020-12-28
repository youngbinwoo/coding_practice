import sys
sys.stdin=open("input.txt", "rt")

num=list(range(21))

for _ in range(10):
    a,b=map(int,input().split())
    for j in range((b-a+1)//2):
        num[a+j],num[b-j]=num[b-j],num[a+j]

for i in num:
    if i>0:
        print(i,end=' ')
