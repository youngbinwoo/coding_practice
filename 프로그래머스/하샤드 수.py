def solution(x):
    Sum=0
    s=str(x)
    for i in range(len(s)):
        Sum+=int(s[i])
    if x%Sum==0:
        return True
    else: 
        return False
