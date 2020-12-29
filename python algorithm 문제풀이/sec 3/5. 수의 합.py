import sys
sys.stdin=open("input.txt", "rt")

m,n=map(int,input().split())
num=list(map(int,input().split()))

a=0
b=1
sum=num[0]
cnt=0
num.append(0)

while b<=m:
    if sum <n :
        sum+=num[b]
        b+=1
    elif sum==n:
        a+=1
        b=a+1
        sum=num[a]
        cnt+=1
    else:
        a+=1
        b=a+1
        sum=num[a]

print(cnt)
