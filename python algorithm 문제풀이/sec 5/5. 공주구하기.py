from collections import deque
import sys
sys.stdin=open("input.txt", "r")
a,b=map(int,input().split())
q=list(range(1,a+1))
q=deque(q)

while q:
    for _ in range(b-1):
        x=q.popleft()
        q.append(x)
    q.popleft()
    if len(q)==1:
        print(q[0])
        q.popleft()

