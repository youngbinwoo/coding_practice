n=int(input())
m=int(input())
ans=abs(n-100)

if m==0:
    ans=min(ans,len(str(n)))
else:
    broken=list(input().split())
    for i in range(1000001):
        f=0
        str_i=str(i)
        for j in str_i:
            if j in broken:
                f=1
                break
        if f==0:
            ans=min(ans,abs(i-n)+len(str_i))
print(ans)
