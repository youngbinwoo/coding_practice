ans=0
def solution(num, t):
    return r_solution(0,0,num,t)

def r_solution(L,s,num, t):
    global ans
    if L==len(num):
        if s==t:
            ans+=1
        return
    r_solution(L+1,s+num[L],num,t)
    r_solution(L+1,s-num[L],num,t)
    return ans
