import sys
#sys.stdin=open("input.txt", "r")

m,p=map(int,input().split())
num=[]
for _ in range(m):
    num.append(list(map(int,input().split())))
w=[0]*(p+1)

for i in  range(m):
    for k in range(num[i][0],p+1):
        w[k]=max(w[k-num[i][0]]+num[i][1],w[k])

print(w[-1])

