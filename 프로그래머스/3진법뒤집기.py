def solution(n):
    num=[]
    ans=0
    
    while n!=0:
        num.append(str(n%3))
        n=n//3
    num.reverse()
    for i in range(len(num)):
        ans+=(3**i)*int(num[i])
        
    return ans
