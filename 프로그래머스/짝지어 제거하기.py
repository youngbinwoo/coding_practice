def solution(s):
    s=list(map(str,s))
    q=[]
    q.append(s[0])
    s.pop(0)
    for i in range(len(s)):
        if len(q)==0 or q[-1]!=s[i]:
            q.append(s[i])
        else:
            q.pop(-1)
    if len(q)==0:
        return 1
    return 0
