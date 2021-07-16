num=int(input())
lis=list(map(int,input().split()))
lis.sort()

if num%2==0:
    m=num//2
    print(lis[m-1]*lis[m])
else:
    m=num//2
    print(lis[m]*lis[m])
