import sys
sys.stdin=open("input.txt", "rt")

n,m=map(int,input().split())
num=list(map(int,input().split()))

rt=1
lt=sum(num)

def Cnt(M):
    cnt=1
    ans=0
    for i in num:
        if ans+i>M:
            cnt+=1
            ans=i
        else: 
            ans+=i
    return cnt

maxx=max(num)
res=0
while rt<=lt:
    M=(rt+lt)//2
    if M>=maxx and Cnt(M)<=m:
        res=M
        lt=M-1
    else:
        rt=M+1

print(res)
