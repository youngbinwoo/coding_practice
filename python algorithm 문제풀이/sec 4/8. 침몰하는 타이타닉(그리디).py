import sys
sys.stdin=open("input.txt", "rt")

n,m=map(int,input().split())
num=list(map(int, input().split()))
num.sort()

cnt=0
for i in range(n):
    if len(num)==1:
        cnt+=1
        break
    if num[-1]+num[0]<=m:
        num.pop()
        num.pop(0)
        cnt+=1
    else:
        num.pop()
        cnt+=1

    if len(num)==0:
        break
print(cnt)
