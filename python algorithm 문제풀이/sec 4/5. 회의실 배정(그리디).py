import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
num=[]

for i in range(n):
    a,b=map(int,input().split())
    num.append((a,b))

num.sort(key=lambda x:x[1])

cnt=1
a=0
b=1
while b<n:
    if num[a][1]<=num[b][0]:
        cnt+=1
        a=b
        b=b+1
    else:
        b=b+1
 
print(cnt)
