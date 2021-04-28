import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
L=[list(map(int,input().split())) for _ in range(n)]
L.sort(reverse=True)
h=[0]*n
h[0]=L[0][1]
for  i in range(1,n):
    m=0
    for j in range(i+1):
        if L[i][0]<L[j][0] and L[i][2]<L[j][2]:
            if h[j]+L[i][1]>m:
                m=h[j]+L[i][1]
            h[i]=m
        elif h[i]==0:
            h[i]=L[i][1]

print(max(h))