def G(x,y):
    global ans
    if y==0:
        print(x)
        print(a*b//x)
        return 
    else:
        x1=min(x,y)
        y1=max(x,y)%min(x,y)
        G(x1,y1)

a,b=map(int,input().split())
G(a,b)
