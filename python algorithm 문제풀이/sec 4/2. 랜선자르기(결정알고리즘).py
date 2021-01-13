import sys
sys.stdin=open("input.txt", "rt")

def Count(len):
    cnt=0
    for i in num:
        cnt+=(i//len)
    return cnt


N,M=map(int,input().split())

num=[]
largest=0
for i in range(N):
    x=int(input())
    num.append(x)
    largest=max(largest,x)

lt=largest
rt=1
res=0
while rt<=lt:
    mid=(rt+lt)//2
    if Count(mid)>=M:
        res=mid
        rt=mid+1
    else:
        lt=mid-1
print(res)
