def solution(table, L, preference):
    D=dict()
    T=[]
    for i in range(len(table)):
        T.append(table[i].split())
    
    for i in range(len(T)):
        A=0
        for k in range(len(L)):
            for j in range(1,len(T[i])):
                if L[k]==T[i][j]:
                    A+=(6-j)*preference[k]
        D[T[i][0]]=A
        
    score=D.values()
    M=max(score)
    ans=[]
    for key,value in D.items():
        if M==value:
            ans.append(key)
    ans.sort()
    return ans[0]
