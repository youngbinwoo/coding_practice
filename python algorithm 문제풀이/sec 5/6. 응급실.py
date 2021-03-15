from collections import deque
import sys
sys.stdin=open("input.txt", "r")
a,b=map(int,input().split())
q=[(pos, val) for pos, val in enumerate (list(map(int,input().split())))]
q=deque(q)
cnt=0

while True:
    cur=q.popleft()
    if any(cur[1]<x[1] for x in q):
        q.append(cur)
    else:
        cnt+=1
        if cur[0]==b:
            break
print(cnt)
