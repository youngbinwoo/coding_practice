def solution(arr1, arr2):
    ans=[]
    for i in range(len(arr1)):
        r_ans=[]
        for j in range(len(arr1[0])):
            r_ans.append(arr1[i][j]+arr2[i][j])
        ans.append(r_ans)
    return ans
