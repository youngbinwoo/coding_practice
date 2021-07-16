def TM(L,S,R):
    if L==n:
        if len(S)!=n//2 or len(R)!=n//2:
            return -1
        if len(S)==n//2 and len(R)==n//2:
            s=r=diff=0
            for i in range(n//2):
                for j in range(n//2):
                    if i!=j:
                        s+=num[S[i]][S[j]]
                        r+=num[R[i]][R[j]]
            diff=abs(s-r)
            return diff

    if len(S)>n//2 or len(R)>n//2:
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
