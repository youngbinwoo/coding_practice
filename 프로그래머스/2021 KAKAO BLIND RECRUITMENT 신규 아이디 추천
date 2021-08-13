def solution(new_id):
    ans=[]
    
    # 1단계, 2단계, 3단계, 4단계 중 처음 위치된 . 제거
    be='.'
    for i in new_id:
        if i=='.' and i==be:
            continue
        if i.isalpha()==False and i.isdigit()==False and i!='-' and i!='_' and i!='.':
            continue
        else:
            ans.append(i.lower())
        be=i
    
    # ans이 . 만 이루어졌을 때, 제거
    if len(ans)==1 and ans[0]=='.':
        ans.pop(0)
            
    # 4단계 중 끝에 .이 위치한 경우 제거하는 것 충족
    for i in range(len(ans)-1,0,-1):
        if ans[i]!='.':
            break
        if ans[i]=='.':
            ans.pop(i)
    
    # 5단계 충족
    if len(ans)==0:
        ans.append('a')
    
    # 6단계 충족
    if len(ans)>15: 
        ans=ans[:15]
        for i in range(len(ans)-1,0,-1):
            if ans[i]!='.':
                break
            if ans[i]=='.':
                ans.pop(i)
                
    # 7단계 충족
    if len(ans)<3: 
        while len(ans)<3:
            ans.append(ans[-1])
    return ''.join(map(str,ans))
