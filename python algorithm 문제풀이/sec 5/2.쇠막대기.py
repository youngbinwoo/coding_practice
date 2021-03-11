import sys
sys.stdin=open("input.txt", "r")
a=input()
stack=[]
sum=0

for i in range(len(a)):
    if a[i]=='(':
        stack.append(a[i])
    else:
        if a[i-1]=='(' :
            stack.pop()
            sum+=len(stack)
        else:
            stack.pop()
            sum+=1

print(sum)
