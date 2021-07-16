import sys
num=[]
for _ in range(9):
    num.append(int(input()))
num.sort()
a=0
b=0

for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        s=sum(num)
        if s-(num[i]+num[j])==100:
            a=num[i]
            b=num[j]
            num.remove(a)
            num.remove(b)
            print('\n'.join(map(str,num)))
            sys.exit(0)
