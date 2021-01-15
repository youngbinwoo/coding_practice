import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
num=[]

for i in range(n):
    a,b=map(int,input().split())
    num.append((a,b))
num.sort()
num.reverse()


cnt=0
et=0
for a,b in num:
    if b>et:
        et=b
        cnt+=1

print(cnt)
