def getnumber(stack,num,r_num,ch):
    if stack:
        r_num.add(int(''.join(stack)))        
    for i in range(len(num)):
        if ch[i]==0:
            ch[i]=1
            stack.append(num[i])
            getnumber(stack,num,r_num,ch)
            ch[i]=0
            stack.pop()
    return list(r_num)
        
def solution(num):
    ch=[0]*len(num)
    num=list(map(str,num))
    num=getnumber([],num,set(),ch)
    
    r_ans=0
    for k in num:
        ans=0
        if k!=1 and k!=0:
            for i in range(1,(k+1)//2+1):
                if k%i==0:
                    ans+=1
        if ans==1:
            r_ans+=1
            
    return r_ans
