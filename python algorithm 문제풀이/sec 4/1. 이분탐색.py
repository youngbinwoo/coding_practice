import sys
#sys.stdin=open("input.txt", "rt")
N,M=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
rt=0
lt=N-1

for i in range(N):
    mid=(rt+lt)//2
    if a[mid]==M:
        ans=mid+1
        break
    elif a[mid]>M:
        lt=mid-1
    else:
        rt=mid+1
print(ans)
