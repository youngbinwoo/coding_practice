import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

r=[]
c=0
d=0
for i in range(n):
    b=0

    r.append(sum(a[i]))
    for j in range(n):
        b+=a[j][i]
        if i==j:
            c+=a[i][j]
        if i+j==4:
            d+=a[i][j]
    r.append(b)
r.append(c)
r.append(d)
print(max(r))

__________________________________________________________________________________________________

import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
largest=-21470000
for i in range(n):
    sum1=sum2=0
    for j in ragne(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2

sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2

    
