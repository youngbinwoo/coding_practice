def solution(s):
    n=''
    ans=''
    for i in s:
        if i.isdigit()==True:
            ans+=str(i)
        else:
            n=n+i
            if n=='zero':
                ans+='0'
                n=''
            elif n=='one':
                ans+='1'
                n=''
            elif n=='two':
                ans+='2'
                n=''
            elif n=="three":
                ans+='3'
                n=''
            elif n=="four":
                ans+='4'
                n=''
            elif n=="five":
                ans+='5'
                n=''
            elif n=="six":
                ans+='6'
                n=''
            elif n=="seven":
                ans+='7'
                n=''
            elif n=="eight":
                ans+='8'
                n=''
            elif n=="nine":
                ans+='9'
                n=''
    return int(ans)
