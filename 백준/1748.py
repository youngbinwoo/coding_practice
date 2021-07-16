n=int(input())
ans=0
L=len(str(n))
s=0
if len(str(n))==1:
    s=n
else:
    s+=(n-10**(L-1)+1)*L
    for i in range(1,L):
        s+=9*10**(i-1)*i
print(s)
