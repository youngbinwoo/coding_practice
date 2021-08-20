import heapq
def solution(s, K):
    #!
    heapq.heapify(s)
    ans=0
    while s[0]<K:
        ans+=1
        a=heapq.heappop(s)+heapq.heappop(s)*2
        heapq.heappush(s,a)
        if len(s)==2 and s[0]<K and s[1]<K and s[0]+s[1]*2<K:
            return -1
    return ans
