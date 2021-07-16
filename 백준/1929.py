a,b=map(int,input().split())
b=max(a,b)
a=min(a,b)
D=[1]*(b+1)
for i in range(2,b+1):
    j=1
    while i*j<b+1:
       D[i*j]+=1
       j+=1

for i in range(a,b+1):
    if D[i]==2:
        print(i)
