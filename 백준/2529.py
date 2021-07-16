def D(x,y,op):
    if op=='<':
        if x>y:
            return False
    if op=='>':
        if x<y:
            return False
    return True

def DFS(L,ans):
    if L==n+1:
        ANS.append(ans)
        return
    for i in range(10):
       if ch[i]==1:
           continue
       if L==0 or D(ans[L-1],str(i),bu[L-1]):
             ch[i]=1
             DFS(L+1,ans+str(i))
             ch[i]=0


n=int(input())
bu=input().split()
ANS=[]
ch=[0]*10
DFS(0,'')
print(ANS[-1],ANS[0],sep='\n')
