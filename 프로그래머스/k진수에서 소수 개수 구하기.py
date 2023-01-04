#진수변환
def conversion(n, k):
    p=''
    while n!=0:
        p+=str(n%k)
        n=n//k        
    p=p[::-1]
    p=p.split('0')
    return p
    
#소수체크
def prime_check(n):
    if n==1:
        return False
    else:  
        for i in range(2,int(n**0.5)+1):
            if n%i ==0:
                return False
        return True

def solution(n, k):
    p=conversion(n,k)
    ans=0
    for x in p:
        if prime_check(int(x)) == True:
            ans+=1
    return ans
