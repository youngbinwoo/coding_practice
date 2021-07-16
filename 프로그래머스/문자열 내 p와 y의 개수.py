def solution(s):
    s=s.lower()
    a_cnt=0
    b_cnt=0
    for i in range(len(s)):
        if s[i]=='p':
            a_cnt+=1
        elif s[i]=='y':
            b_cnt+=1
    if a_cnt==b_cnt or (a_cnt==0 and b_cnt==0):
        return True
    else:
        return False
