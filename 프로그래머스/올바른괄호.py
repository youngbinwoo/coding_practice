def solution(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(s[i])
        else:
            if len(stack)!=0:
                a=stack.pop()
            else:
                return False
                break
    if len(stack)==0:
        return True
    else:
        return False
    
