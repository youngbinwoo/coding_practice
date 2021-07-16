def DFS(L):
    global A,B,before
    if L==a:
        A=B=0
        for i in range(len(ans)):
            if ans[i] in M:
                A+=1
            else:
                B+=1

        if A>=1 and B>=2:
            print(''.join(ans))


    else:
        for i in range(len(s)):
            if ch[i]==0 and s[i]>=before:
                before=s[i]
                ch[i]=1
                ans[L]=s[i]
                DFS(L+1)
                ch[i]=0
                before='a'

if __name__=="__main__":
    a,b=map(int,input().split())
    s=list(map(str,input().split()))
    s.sort()
    before='a'
    ch=[0]*b
    ans=[0]*a
    M=['a','e','i','o','u']
    DFS(0)
