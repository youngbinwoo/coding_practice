import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
c=list(map(int,input().split()))
m=int(input())

w=[0]*(m+1)

for i in  range(len(c)):
    for k in range(c[i],m+1):
        if w[k]!=0 and w[k-c[i]]+1>w[k]:
            w[k]=w[k]
        else:
            w[k]=w[k-c[i]]+1

print(w[-1])