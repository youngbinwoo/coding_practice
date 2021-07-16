def solution(a, b):
    c=0
    ans=[]
    if a>b:
        for i in range(b,a+1):
            c+=i
        ans.append(c)

        return ans[0]
    elif a<b:
        for i in range(a,b+1):
            c+=i
        ans.append(c)

        return ans[0]
    else:
        return a
