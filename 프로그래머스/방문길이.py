def solution(dirs):
    x=y=0
    distance=set()
    
    for i in dirs:
        if i=='U':
            xx=x
            yy=y+1
        elif i=='L':
            xx=x-1
            yy=y
        elif i=='R':
            xx=x+1
            yy=y
        else:
            xx=x
            yy=y-1
            
        if -5<=xx<=5 and -5<=yy<=5:
            start=(x,y,xx,yy)
            end=(xx,yy,x,y)
            if start not in distance:
                distance.add(start)
                distance.add(end)        
            x=xx
            y=yy
    return len(distance)//2
