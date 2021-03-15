import sys
sys.stdin=open("input.txt", "r")
a=input()
stack=[]


for x in a:
    if x.isdecimal():
        stack.append(x)
    else:
        if x=='+':
            r=int(stack[-2])+int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(r)
        elif x=='-':
            r=int(stack[-2])-int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(r)
        elif x=='*':
            r=int(stack[-2])*int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(r)
        else:
            r=int(stack[-2])/int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(r)


for i in stack:
    print(i)
