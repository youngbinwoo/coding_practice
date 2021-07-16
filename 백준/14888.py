def solution(a,L,cur,plus,minus,mul,div):
    global Max,Min
    if L==len(a):
        if cur>Max:
            Max=cur
        if cur<Min:
            Min=cur
    #plus
    if plus>0:
        solution(a,L+1,cur+a[L],plus-1,minus,mul,div)

    #minus
    if minus>0:
        solution(a,L+1,cur-a[L],plus,minus-1,mul,div)
    #mul
    if mul>0:
        solution(a,L+1,cur*a[L],plus,minus,mul-1,div)
    #div
    if div>0:
        if cur>=0:
            solution(a,L+1,cur//a[L],plus,minus,mul,div-1)
        else:
            solution(a,L+1,-(cur//-a[L]),plus,minus,mul,div-1)

n=int(input())
num=list(map(int,input().split()))
arr=list(map(int,input().split()))
Max=-10000000000000
Min=100000000000000
solution(num,1,num[0],arr[0],arr[1],arr[2],arr[3])
print(Max)
print(Min)
