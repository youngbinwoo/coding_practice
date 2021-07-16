def solution(N, stages):
    ans=[]
    b=len(stages)
    ans=dict()
    r_ans=[]
    for i in range(1,N+1):
        if b==0:
            ans[i]=0
            continue
        a=0
        for j in range(len(stages)):
            if i ==stages[j]:
                a+=1
        if b!=0:
            ans[i]=a/b
            b=b-a
        else:
            ans[i]=0
            break
    return sorted(ans,key=lambda x: ans[x], reverse=True)
