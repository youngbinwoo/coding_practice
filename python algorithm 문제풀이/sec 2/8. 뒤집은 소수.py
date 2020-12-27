1. def 안에 return으로 종결하면 답이 안나오고, print로 끝내면 답이 나온다.. 

import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
a=list(map(str,input().split()))

def reverse(x):
    return x[::-1]

def isPrime(x):
    ans=0
    for i in range(1,x+1):
        if x%i==0:
            ans+=1
    if ans==2:
        print(x, end=' ')

for x in a:
    rev=reverse(x)
    rev=int(rev)
    r_ans=isPrime(rev)
    
_____________________________________________________________________________
2. 조금 바꾸면 정답이 됨 

import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
a=list(map(int,input().split()))

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res


def isPrime(x):
    ans=0
    for i in range(1,x+1):
        if x%i==0:
            ans+=1
    if ans==2:
        return True

for x in a:
    rev=reverse(x)
    if isPrime(rev):
        print(rev,end=' ')
        
__________________________________________________________________
3. 정답

import sys
#sys.stdin=open("input.txt", "rt")

n=int(input())
a=list(map(int,input().split()))

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res


def isPrime(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    else:
        return True


for x in a:
    rev=reverse(x)
    if isPrime(rev):
        print(rev,end=' ')
