import sys
#sys.stdin=open("input.txt", "rt")
ans=[]

n,k=map(int,input().split())

num=list(map(int,input().split()))

for i in range(n-2):
    for j in range(i+1,n-1):
        for p in range(j+1,n):
            a=num[i]+num[j]+num[p] 
            ans.append(a)
r_ans=list(set(ans))
r_ans.sort(reverse=True)
print(r_ans[k-1])
