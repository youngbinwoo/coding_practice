1. Timeover

import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
r_ans=0

for i in range(1,n+1):
    ans=0
    for j in range(1,i+1):
        if i%j==0:
            ans+=1
    if ans==2:
        r_ans+=1
print(r_ans)

___________________________________________

2. 답 오류

import sys
#sys.stdin=open("input.txt", "rt")

n=int(input())

ans=0
for i in range(2,n+1):
    if i!=2 and i%2==0:
        continue
    elif i!=3 and i%3==0:
        continue
    elif i!=5 and i%5==0:
        continue
    elif i!=7 and i%7==0:
        continue
    else:
        ans+=1
print(ans)

___________________________________________

3. 정답

import sys
sys.stdin=open("input.txt", "rt")

n=int(input())

an=[0]*(n+1)
ans=0

for i in range(2,n+1):
    if an[i]==0:
        ans+=1
        for j in range(i,n+1,i):
            an[j]=1
print(ans)

