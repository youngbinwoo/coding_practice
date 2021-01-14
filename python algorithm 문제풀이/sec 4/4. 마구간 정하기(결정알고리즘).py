import sys
sys.stdin=open("input.txt", "rt")

n,m=map(int,input().split())

num=[]
for i in range(n):
    a=int(input())
    num.append(a)
num.sort()

def mar(mid):
    cnt=1
    a=0
    b=0
    for _ in range(n):
        if num[b]-num[a]>=mid:
            cnt+=1
            a=b
            b=a+1
        else:
            b+=1

    return cnt


rt=min(num)
lt=max(num)

res=0
while rt<=lt:
    mid=(rt+lt)//2
    if mar(mid)>=m:
        rt=mid+1
        res=mid
    else:
        lt=mid-1
print(res)
