import sys
sys.stdin=open("input.txt", "rt")

n,m=map(int,input().split())
num=list(map(int,input().split()))

rt=1
lt=sum(num)

def Cnt(M):
    cnt=1
    ans=[]
    for i in range(n):
        ans.append(num[i])
        if sum(ans)>M:
            cnt+=1
            ans=[num[i]]
    return cnt

res=0
while rt<=lt:
    M=(rt+lt)//2
    if Cnt(M)<=m:
        res=M
        lt=M-1
    else:
        rt=M+1

print(res)
