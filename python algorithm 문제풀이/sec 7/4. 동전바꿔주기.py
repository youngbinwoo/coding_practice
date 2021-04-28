import sys
sys.stdin=open("input.txt", "r")

def DFS(l,s):
    global cnt
    if s>T:
        return 
    if l==k:
        if s==T:
            cnt+=1
    else:
        for i in range(n[l]+1):
            DFS(l+1,s+c[l]*i)

if __name__=="__main__":
    T=int(input())
    k=int(input())
    c=[]
    n=[]
    for i in range(k):
        a,b=input().split()
        c.append(int(a))
        n.append(int(b))
    cnt=0
    DFS(0,0)
    print(cnt)
