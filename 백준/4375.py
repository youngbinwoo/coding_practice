while True:
    try:
        num=int(input())
        a=0
        while True:
            a+=1
            if int('1'*a)%num==0:
                print(a)
                break
    except:
        break
