def solution(a, b):
    s=0
    if a!=1:
        for a in range(1,a):
            if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
                s+=31
            elif a==2:
                s+=29
            else:
                s+=30

    div=(s+b)%7
    if div==1:
        return 'FRI'
    elif div==2:
        return 'SAT'
    elif div==3:
        return 'SUN'
    elif div==4:
        return 'MON'
    elif div==5:
        return'TUE'
    elif div==6:
        return 'WED'
    elif div==0:
        return 'THU'
