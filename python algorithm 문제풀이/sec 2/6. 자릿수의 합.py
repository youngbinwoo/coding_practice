import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
a=list(map(int,input().split()))

def digit_sum(x):
    r_sum=0
    for i in str(x):
        r_sum+=int(i)
    return r_sum

max=-21470000
for x in a:
    top=digit_sum(x)
    if max<top:
        max=top
        res=x

print(res)

