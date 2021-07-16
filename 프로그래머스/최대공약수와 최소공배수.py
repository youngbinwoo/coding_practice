def solution(n, m):
    M1=0
    ans=[]
    for i in range(1,m+1):
        if n%i==0 and m%i==0:
            if i>M1:
                M1=i
    ans.append(M1)
    M2=(n*m)//M1
    ans.append(M2)
    return ans
