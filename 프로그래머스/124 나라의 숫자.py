def solution(n):
    ans=[]
    num=['1','2','4']
    if n==1:
        return '1'
    elif n==2:
        return '2'
    elif n==3:
        return '4'
    else:
        while n>3:
            a=n%3
            if a==0:
                n=n//3-1
                ans.insert(0,num[2])
            else:
                n=n//3
                ans.insert(0,num[a-1])
            if n<4:
                ans.insert(0,num[n-1])         
        return ''.join(map(str,ans))
