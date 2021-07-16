def solution(n):
    n=str(n)
    ans=0
    for i in range(len(n)):
        ans+=int(n[i])
        
    return ans
