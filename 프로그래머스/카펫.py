def solution(brown, yellow):
    if yellow==1:
        return [3,3]
    for i in range(1,yellow):
        garo=yellow//i
        sero=i
        if garo*sero==yellow:
            ans=0
            #대각선 크기
            ans+=4
            #양 옆 크기
            ans+=sero*2
            #위 아래 크기
            ans+=garo*2
        if ans==brown:
            r_ans=[garo+2,sero+2]
            return r_ans
