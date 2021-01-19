import sys
#sys.stdin=open("input.txt", "r")
a,b=map(int, input().split())
num=list(map(int,str(a)))
stack=[]

for x in num:
    while stack and b>0 and stack[-1]<x:
        stack.pop()
        b-=1
    stack.append(x)

if b!=0:
    stack=stack[-len(num):-b]

for i in stack:
    print(i,end='')