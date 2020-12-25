import sys
#sys.stdin=open("input.txt", "rt")

ans=[]
re_ans=[]

n=int(input())
num=list(map(int,input().split()))

avg=round(sum(num)/n)

for i in range(n):
    ans.append(abs(num[i]-avg))
    r_ans=min(ans)

for i in range(n):
    if ans[i]==r_ans:
        re_ans.append(num[i])

ree_ans=max(re_ans)
for i in range(n):
    if num[i]==ree_ans:
        print("%d %d" %(avg,i+1))
        break





