def solution(s):
    s=list(map(int,s.split()))
    Min=min(s)
    Max=max(s)
    ans=""
    ans+=str(Min)
    ans+=' '
    ans+=str(Max)
    return ans
