def solution(numbers):
    ans=[]
    for i in range(len(numbers)):
        for j in range(i,len(numbers)-1):
            ans.append(numbers[i]+numbers[j+1])
            ans=set(ans)
            ans=list(ans)
            ans.sort()
    return ans
