M=1000000

D=[1]*(M+1)
S=[0]*(M+1)
for i in range(2,M+1):
    j=1
    while i*j<M+1:
       D[i*j]+=i
       j+=1
for j in range(1,M+1):
    S[j]+=S[j-1]+D[j]

n=int(input())
ans=[]
for _ in range(n):
    a=int(input())
    ans.append(S[a])

print('\n'.join(map(str,ans)))
