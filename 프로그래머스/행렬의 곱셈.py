def solution(arr1, arr2):
    ans = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(ans)):
        for j in range(len(ans[0])):
            for k in range(len(arr2)):
                ans[i][j]+=arr1[i][k]*arr2[k][j]
    return ans
