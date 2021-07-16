def TM(L,S,R):
    if L==n:
        if len(S)==0 or len(R)==0:
            return -1
        if len(S)>0 and len(R)>0:
            s=r=diff=0
            if len(S)==len(R):
                for i in range(len(S)):
                    for j in range(len(S)):
                        if i!=j:
                            s+=num[S[i]][S[j]]
                            r+=num[R[i]][R[j]]
            else:
                for i in range(len(S)):
                    for j in range(len(S)):
                        if i!=j:
                            s+=num[S[i]][S[j]]
                for i in range(len(R)):
                    for j in range(len(R)):
                        if i!=j:
                            r+=num[R[i]][R[j]]
            diff=abs(s-r)
            return diff
    if len(S)>n-1 and len(R)>n-1:
        return -1

    ans=-1
    T1=TM(L+1,S+[L],R)
    if ans==-1 or (T1!=-1 and ans>T1):
        ans=T1
    T2=TM(L+1,S,R+[L])
    if ans==-1 or (T2!=-1 and ans>T2):
        ans=T2
    return ans


if __name__=="__main__":
    n=int(input())
    num=[list(map(int,input().split())) for _ in range(n)]
    print(TM(0,[],[]))
