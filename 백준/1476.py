d=list(map(int,input().split()))

a=b=c=n=1
while True:
    if a==d[0] and b==d[1] and c==d[2]:
        break
    else:
        a+=1
        b+=1
        c+=1
        if a==16:
            a=1
        if b==29:
            b=1
        if c==20:
            c=1
        n+=1
print(n)
