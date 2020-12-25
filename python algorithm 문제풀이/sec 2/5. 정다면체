import sys
sys.stdin=open("input.txt", "rt")

ans=[]
n,m=map(int,input().split())
max=0


for i in range(1, n+1):
    for j in range(1,m+1):
        ans.append(i+j)
        r_ans=list(set(ans))

for i in range(len(r_ans)):
    if ans.count(r_ans[i])>max:
        max=ans.count(r_ans[i])

for i in range(len(r_ans)):
    if ans.count(r_ans[i])==max:
        print(r_ans[i], end=' ')
        
 _________________________________
 import sys
sys.stdin=open("input.txt", "rt")

n,m=map(int,input().split())
cnt=[0]*(n+m+3)


for i in range(1, n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1

for i in range(len(cnt)):
    if cnt[i]==max(cnt):
        print(i,end=' ')
