import sys
sys.stdin=open("input.txt", "rt")
a=[list(map(int,input().split())) for _ in range(7)]

cnt=0
for i in range(len(a[0])):
    for j in range(len(a[0])//2):
        if a[i][j]==a[i][j+4] and a[i][j+1]==a[i][j+3]:
            cnt+=1
for j in range(len(a[0])):
    for i in range(len(a[0])//2):
        if a[i][j]==a[i+4][j] and a[i+1][j]==a[i+3][j]:
            cnt+=1

print(cnt)


___________________________________________________________________

import sys
sys.stdin=open("input.txt", "rt")
a=[list(map(int,input().split())) for _ in range(7)]

cnt=0
for i in range(3):
    for j in range(7):
        tmp=a[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2):
            if a[i+k][j]!=a[i-k+4][j]:
                break
        else:
            cnt+=1

print(cnt)
