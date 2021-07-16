import sys
n=int(input())
D=[]
f=0
b=0

for i in range(n):
    command=sys.stdin.readline().split()

    if command[0]=='push':
        b+=1
        D.append(int(command[1]))

    elif command[0]=='pop':
        if f==b:
            print(-1)
        else:
            print(D.pop(f))
            b-=1

    elif command[0]=='size':
        print(len(D))

    elif command[0]=='empty':
        if b==f:
            print(1)
        else:
            print(0)

    elif command[0]=='front':
        if b==f:
            print(-1)
        else:
            print(D[f])

    elif command[0]=='back':
        if f==b:
            print(-1)
        else:
            print(D[b-1])
