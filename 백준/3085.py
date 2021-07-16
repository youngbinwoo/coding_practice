n=int(input())
c=list(list(input()) for _ in range(n))
def check(c):
    ans=1
    for i in range(n):
        cnt=1
        for j in range(1,n):
            if c[i][j]==c[i][j-1]:
                cnt+=1
            else:
                cnt=1
            if cnt>ans:
                ans=cnt

    for i in range(n):
        cnt=1
        for j in range(1,n):
            if c[j][i]==c[j-1][i]:
                cnt+=1
            else:
                cnt=1
            if cnt>ans:
                ans=cnt
    return ans

ans=0
for i in range(n):
    for j in range(n):
        if j+1<n:
            c[i][j],c[i][j+1]=c[i][j+1],c[i][j]
            t=check(c)
            if t>ans:
                ans=t
            c[i][j],c[i][j+1]=c[i][j+1],c[i][j]

        if j+1<n:
            c[j][i],c[j+1][i]=c[j+1][i],c[j][i]
            t=check(c)
            if t>ans:
                ans=t
            c[j][i],c[j+1][i]=c[j+1][i],c[j][i]

print(ans)
