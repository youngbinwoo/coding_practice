import math
from collections import deque

def solution(progresses, speeds):
    q=[]
    for i in range(len(progresses)):
        ans=(100-progresses[i])/speeds[i]
        q.append(math.ceil(ans))

    r_ans=[]
    cnt=0
    a=q[0]
    for j in range(len(q)):
        if q[j]<=a:
            cnt+=1
        else:
            r_ans.append(cnt)
            a=q[j]
            cnt=1
    r_ans.append(cnt)
    return r_ans
