import sys
sys.stdin=open("input.txt", "rt")

N,K =map(ins,input().split())


ans=[]

for i in range(1, N+1):
    if N%i==0:
        ans.append(i)
    
if len(ans)>=K:
    r_ans=ans[K-1]
else:
    r_ans=-1

print(r_ans)