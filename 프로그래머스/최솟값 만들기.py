def solution(A,B):
    ans=0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        ans+=A[i]*B[i]
    return ans
