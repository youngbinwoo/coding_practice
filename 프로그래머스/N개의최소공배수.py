def solution(arr):
    m=1
    for i in range(len(arr)):
        m=m*arr[i]

    for j in range(1,m+1):
        cnt=0
        for z in range(len(arr)):
            if j%arr[z]==0:
                cnt+=1
        if cnt==len(arr):
            return j
            break
