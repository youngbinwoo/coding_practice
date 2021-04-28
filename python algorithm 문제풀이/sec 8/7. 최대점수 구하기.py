import sys
#sys.stdin=open("input.txt", "r")

m,p=map(int,input().split())
num=[]

for _ in range(m):
    num.append(list(map(int,input().split())))
w=[0]*(p+1)


for i in  range(len(num)):
    for k in range(p,num[i][1]-1,-1):
        w[k]=max(w[k],w[k-num[i][1]]+num[i][0])
print(w[-1])