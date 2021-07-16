n=int(input())
L=list(map(int,input().split()))


r_ans=0
for i in L:
    ans=0
    for j in range(1,i+1):
        if i%j==0:
            ans+=1
    if ans==2:
        r_ans+=1

print(r_ans)
