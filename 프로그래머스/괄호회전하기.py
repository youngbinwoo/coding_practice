def solution(s):
    s=list(s)
    ans=0
    for i in range(len(s)):
        stack=[]
        A=0
        if i==0:
            s=s
        else:
            A=s.pop(0)
            s.append(A)
        for j in range(len(s)):
            if s[j]=='[' or s[j]=='(' or s[j]=='{':
                stack.append(s[j])
            else:
                if len(stack)!=0 and s[j]==']' and stack[-1]=='[':
                    A=1
                    stack.pop()
                elif len(stack)!=0 and s[j]=='}' and stack[-1]=='{':
                    A=1
                    stack.pop()
                elif len(stack)!=0 and s[j]==')' and stack[-1]=='(':
                    A=1
                    stack.pop()
        if A==1 and len(stack)==0:
            ans+=1
    return ans
