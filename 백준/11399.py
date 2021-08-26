n=int(input())
num=list(map(int,input().split()))
num.sort()
ans=0
r_ans=0
for i in range(len(num)):
    ans+=num[i]
    r_ans+=ans
print(r_ans)
