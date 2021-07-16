M=1000000
L=[1]*(M+1)
for i in range(2,M+1):
    j=1
    while i*j<=M:
        L[i*j]+=1
        j+=1


while True:
    n=int(input())
    if n==0:
        break
    for i in range(3,n+1,2):
        if L[i]==2 and  L[n-i]==2:
                print('%d = %d + %d' %(n,i,(n-i)))
                break
