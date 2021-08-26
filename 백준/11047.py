n,m=map(int,input().split())
coin=[int(input()) for _ in range(n)]
coin.sort(reverse=True)

ans=0
for i in range(len(coin)):
    if m>=coin[i]:
        ans+=m//coin[i]
        m-=m//coin[i]*coin[i]
print(ans)
