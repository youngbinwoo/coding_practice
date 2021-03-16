import sys
from collections import deque
sys.stdin=open("input.txt", "r")
n=int(input())

name=[]
for i in range(n):
    name.append(input())

name=deque(name)

for i in range(n-1):
    x=input()
    if x in name:
        while x!=name[0]:
            z=name.popleft()
            name.append(z)
        else:
            name.popleft()
print(name[0])
