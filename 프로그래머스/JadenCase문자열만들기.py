def solution(s):
    ans=''
    f=0
    for i in range(len(s)):
        if f==0 and s[i]!=' ':
            ans+=s[i].upper()
            f=1
        elif f==1 and s[i]!=' ':
            ans+=s[i].lower()
            f=1
        if s[i]==' ':
            ans+=s[i]
            f=0
    return ans
