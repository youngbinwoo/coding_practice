import sys
sys.stdin=open("input.txt", "rt")
ans=[]

t=int(input())
for i in range(1,t+1):
    n,s,e,k=map(int,input().split())
    num=list(map(int,input().split()))
    ans=num[s-1:e]
    ans.sort()
    r_ans=ans[k-1]

    print("#%d %" %(i,r_ans))
