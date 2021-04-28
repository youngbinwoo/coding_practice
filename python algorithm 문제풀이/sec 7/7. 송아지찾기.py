import sys
from collections import deque
sys.stdin=open("input.txt", "r")

s,e=map(int,input().split())
max=10000
dq=deque()
dis=[0]*max
ch=[0]*max
ch[s]=1
dis[s]=0
dq.append(s)

while dq:
    now=dq.popleft()
    if now==e:
        break
    for next in (now-1,now+1,now+5):
        if 0<next<=max:
            if ch[next]==0:
                ch[next]=1
                dis[next]=dis[now]+1
                dq.append(next)
              
print(dis[e])
