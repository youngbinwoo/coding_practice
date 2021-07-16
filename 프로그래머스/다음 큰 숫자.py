def solution(n):
    cnt=0
    m=n
    while m>0:
        if m%2==1:
            cnt+=1
        m=m//2

    for i in range(n+1,n*2+1):
        k=i
        r_cnt=0
        while k>0:
            if k%2==1:
                r_cnt+=1
            k=k//2
        if r_cnt==cnt:
            return i
            break
