def solution(n):
    ans=[]
    if n<2:
        return n
    else:
        for i in range(n+1):
            if i<2:
                ans.append(i)
            else:
                ans.append((ans[-2]+ans[-1])%1234567)
        return ans[-1]
