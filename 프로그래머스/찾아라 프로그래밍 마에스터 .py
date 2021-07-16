def solution(nums):
    a=len(list(set(nums)))
    if a==len(nums)//2:
        return a
    elif a>len(nums)//2:
        return len(nums)//2
    else: 
        return a
