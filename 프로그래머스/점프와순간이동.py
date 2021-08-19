r_ans=0
rr_ans=0
def solution(n):
    global r_ans,rr_ans
    ans=[0,1,1,2]
    if n<=3:
        rr_ans=ans[n]+r_ans
        return rr_ans
    if n%2==0:
        solution(n//2)
    else:
        r_ans+=1
        solution((n-1)//2)
    return rr_ans
