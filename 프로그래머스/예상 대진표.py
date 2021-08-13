def solution(n,a,b):
    if a>b:
        a,b=b,a
    
    ans=1
    while a!=0:
        if a%2==1 and b%2==0 and b-a==1:
            return ans
        if a%2==0:
            a=a//2
        else:
            a=(a+1)//2
        if b%2==0:
            b=b//2
        else:
            b=(b+1)//2
        ans+=1
