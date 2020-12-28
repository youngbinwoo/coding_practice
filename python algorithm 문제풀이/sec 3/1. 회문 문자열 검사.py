import sys
sys.stdin=open("input.txt", "rt")

n=int(input())

for i in range(1,n+1):
    a=input()
    a=str(a)
    a=a.lower()
    if a==a[::-1]:
        ans='YES'
    else:
        ans='NO'
    print('#%d %s' %(i,ans))
        









