def BEFORE(a):
    #a가 0 개일 때, -1 출력되는 것 방지
    if len(a)==0:
        return True
    
    #i값 , j 값 구하기
    i=n-1
    while i>0 and a[i-1]<=a[i]:
        i-=1
    
    if i<=0:
        return False

    j=n-1
    while a[i-1]<=a[j]:
        j-=1

    a[i-1],a[j]=a[j],a[i-1]

    j=n-1
    while i<j:
        a[i],a[j]=a[j],a[i]
        i+=1
        j-=1

    return True

n=int(input())
a=list(map(int,input().split()))
if BEFORE(a):
    print(' '.join(map(str,a)))
else:
    print(-1)
