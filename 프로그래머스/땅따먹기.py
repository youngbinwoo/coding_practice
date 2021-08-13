def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            a=land[i-1][j]
            land[i-1][j]=0
            land[i][j]+=max(land[i-1])
            land[i-1][j]=a
    return max(land[-1])
