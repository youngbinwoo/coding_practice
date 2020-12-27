import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
a=list(map(int,input().split()))

score=0

for i in range(n):
    if a[i]==1:
        for j in range(i,-1,-1):
            if a[j]==1:
                score+=1
            else:
                break

print(score)
