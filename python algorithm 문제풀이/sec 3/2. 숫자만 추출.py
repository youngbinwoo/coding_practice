import sys
sys.stdin=open("input.txt", "rt")

n=input()
num=[]
ans=0
r_ans=0

for i in n:
    if i.isdecimal()==True:
        i=int(i)
        num.append(i)
for i in range(len(num)):
    ans+=num[i]*(10**(len(num)-(i+1)))

for i in range(1,ans+1):
    if ans%i==0:
        r_ans+=1
print(ans)
print(r_ans)

______________________________________________________________
import sys
sys.stdin=open("input.txt", "rt")

n=input()
num=0

for i in n:
    if i.isdecimal()==True:
        num=num*10+int(i) #좋은 방법
print(num)

cnt=0
for i in range(1,num+1):
    if num%i==0:
        cnt+=1
print(cnt)
