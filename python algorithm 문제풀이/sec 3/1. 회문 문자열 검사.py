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
        
_______________________________________________
import sys
sys.stdin=open("input.txt", "rt")

n=int(input())

for i in range(0,n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break
        else:
            print("#%d YES" %(i+1))







