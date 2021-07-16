from collections import deque
n,m,start=map(int, input().split())
num=[[] for _ in range(n+1)]
ch=[0]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    num[a].append(b)
    num[b].append(a)

for i in range(n):
    num[i].sort()

def dfs(x):
    global ch
    ch[x]=1
    print(x, end=' ')
    for y in num[x]:
        if ch[y]==0:
            dfs(y)

def bfs(x):
    ch=[0]*(n+1)
    q=deque()
    q.append(x)

    while q:
        z=q.popleft()
        ch[z]=1
        print(z,end=' ')
        for y in num[z]:
            if ch[y]==0:
                ch[y]=1
                q.append(y)

dfs(start)
print()
bfs(start)
print()
