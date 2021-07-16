def solution(arr):
    ans=[]
    for i in arr:
        if len(ans)==0:
            ans.append(i)
        elif i!=ans[-1]:
            ans.append(i)
            a=i
    return ans
