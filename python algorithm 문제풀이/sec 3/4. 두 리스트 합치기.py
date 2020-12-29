import sys
sys.stdin=open("input.txt", "rt")

n1=int(input())
num1=list(map(int,input().split()))
n2=int(input())
num2=list(map(int,input().split()))

ans=[]
a=0
b=0

for _ in range(n1+n2):
    if num1[a]<num2[b]:
        ans.append(num1[a])
        a+=1
    else:
        ans.append(num2[b])
        b+=1
    if a==n1 or b==n2:
        break

if a==n1:
    ans=ans+num2[b:n2]
else:
    ans=ans+num1[a:n1]

for i in ans:
    print(i,end=' ')
