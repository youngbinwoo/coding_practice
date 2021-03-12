import sys
sys.stdin=open("input.txt", "r")
a=input()
s=[]
str=[]

for i in range(len(a)):
    if a[i]=='(':
        s.append(a[i])
    elif a[i]=='*' or a[i]=='/':
        if (len(s)!=0 and s[-1]=='*') or (len(s)!=0 and s[-1]=='/'):
            str.append(s[-1])
            s.pop()
        s.append(a[i])

    elif a[i]=='+' or a[i]=='-':
        while len(s)!=0 and s[-1]!='(':
            str.append(s[-1])
            s.pop()
        s.append(a[i])

    elif a[i]==')':
        for i in range(len(s)):
            str.append(s[-1])
            s.pop()
            if s[-1]=='(':
                s.pop()
                break
    else:
        str.append(a[i])

if len(s)!=0:
    while len(s)>0:
        str.append(s[-1])
        s.pop()

for i in str:
    print(i,end='')
