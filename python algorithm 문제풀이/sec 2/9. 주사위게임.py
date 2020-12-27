import sys
sys.stdin=open("input.txt", "rt")

n=int(input())

ans=[]

for i in range(n):
    a,b,c=map(int,input().split())
    if a==b==c:
        ans.append(10000+a*1000)
    elif a != b!= c:
        num=[a,b,c]
        r_max=max(num)
        ans.append(r_max*100)
    else:
        if a==b: 
            ans.append(1000+a*100)
        elif a==c:
            ans.append(1000+a*100)
        else:
            ans.append(1000+b*100)

print(max(ans))
