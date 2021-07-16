def solution(n, lost, reserve):
    L=[]
    for i in range(len(reserve)):
        if reserve[i] in lost:
            lost.remove(reserve[i])
            L.append(reserve[i])

    for i in range(len(reserve)):
        if reserve[i] not in L:
            if reserve[i]-1 in lost:
                lost.remove(reserve[i]-1)
            elif reserve[i]+1 in lost:
                lost.remove(reserve[i]+1)
    return n-len(lost)
