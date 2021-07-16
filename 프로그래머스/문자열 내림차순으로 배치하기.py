def solution(s):
    ans=[]
    r_ans=""
    for i in range(len(s)):
        ans.append(ord(s[i]))
        ans.sort(reverse=True)
    for j in ans:
        r_ans+=chr(j)
    return r_ans
