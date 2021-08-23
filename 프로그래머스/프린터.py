r_ans=0
ans=0
def solution(p, l):
    global ans,r_ans
    
    key=[i for i in range(len(p))]
    
    while p:
        A=p.pop(0)
        B=key.pop(0)
        C=0
        for i in range(len(p)):
            if p[i]>A:
                C=1
        if C==0:
            ans+=1
            if B==l:
                r_ans=ans
                return r_ans
        else:
            p.append(A)
            key.append(B)
                
    return r_ans
