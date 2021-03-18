import sys
sys.stdin=open("input.txt", "r")
def DFS(L,sum,tsum):
    global m
    if sum+(total-tsum)<m:
        return 
    if sum>kg:
        return
    if L==n:
        if sum>m:
            m=sum
    else:
        DFS(L+1,sum+num[L],tsum+num[L])
        DFS(L+1,sum,tsum+num[L])

if __name__=="__main__":
    kg,n=map(int,input().split())
    num=[0]*n
    for i in range(n):
        num[i]=int(input())
    m=0
    total=sum(num)
    DFS(0,0,0)
    print(m)
