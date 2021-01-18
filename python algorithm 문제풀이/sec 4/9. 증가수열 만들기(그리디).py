import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
num=list(map(int, input().split()))
ans=[]
f=0
cnt=0

if num[0]>num[-1]:
    f=num[-1]
    num.pop(-1)
    cnt+=1
    ans.append('R')
else:
    f=num[0]
    num.pop(0)
    cnt+=1
    ans.append('L')

for i in range(len(num)):
    if len(num)==0:
        break
    if len(num)==1:
        num[0]>f
        num.pop(0)
        cnt+=1
        ans.append('L')
    if (num[0]>f and num[0]<num[-1] and num[-1]>f) or (num[0]>f and num[-1]<f) :
        f=num[0]
        num.pop(0)
        cnt+=1
        ans.append('L')
    if (num[-1]>f and num[-1]<num[0] and num[0]>f) or (num[-1]>f and num[0]<f):
        f=num[-1]
        num.pop(-1)
        cnt+=1
        ans.append('R')
    if num[-1]<f and num[0]<f:
        break

print(cnt)
for i in ans:
    print(i, end='')
