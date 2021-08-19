A1=A2=0
def solution(n, words):
    global A1,A2
    be=[words[0]]
    A=0
    for i in range(1,len(words)):
        if be[-1][-1]!=words[i][0]:
            A=1
            if (i+1)%n==0:
                A1=(i+1)//n
                A2=n
            else:
                A1=(i+1)//n+1
                A2=(i+1)%n
            break
        if words[i] in be:
            A=1
            if (i+1)%n==0:
                A1=(i+1)//n
                A2=n
            else:
                A1=(i+1)//n+1
                A2=(i+1)%n
            break
        be.append(words[i])
        
    if A==1:
        return [A2,A1]
    if A==0:
        return [0,0]
