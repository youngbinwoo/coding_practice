import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
L=list(map(int,input().split()))
dy=[0]*n
dy[0]=1

for i in range(1,n):
    m=0
    for j in range(i+1):
        if L[i]>L[j]:
            if m<dy[j]+1:
                m=dy[j]+1
            dy[i]=m
    if dy[i]==0:
        dy[i]=1
print(max(dy))