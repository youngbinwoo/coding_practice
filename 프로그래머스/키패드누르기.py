def solution(numbers, hand):
    num=[]
    ans=[]
    L=[]
    R=[]
    for i in range(10):
        if i==0:
            num.append([4,2])
        elif i%3==0:
            num.append([((i-1)//3)+1,3])
        else:
            num.append([(i//3)+1,i%3])

    for j in range(len(numbers)):
        if numbers[j]==1 or numbers[j]==4 or numbers[j]==7:
            ans.append('L')
            L.append(num[numbers[j]])
        elif numbers[j]==3 or numbers[j]==6 or numbers[j]==9:
            ans.append('R')
            R.append(num[numbers[j]])
        else:
            if len(L)==0:
                L.append([4,1])
            if len(R)==0:
                R.append([4,3]) 
            if abs(L[-1][0]-num[numbers[j]][0])+abs(L[-1][1]-num[numbers[j]][1])>abs(R[-1][0]-num[numbers[j]][0])+abs(R[-1][1]-num[numbers[j]][1]):
                ans.append('R')
                R.append(num[numbers[j]])
            elif abs(L[-1][0]-num[numbers[j]][0])+abs(L[-1][1]-num[numbers[j]][1])<abs(R[-1][0]-num[numbers[j]][0])+abs(R[-1][1]-num[numbers[j]][1]):
                ans.append('L')
                L.append(num[numbers[j]])
                     
            else:
                if hand=="right":
                    ans.append('R')
                    R.append(num[numbers[j]])
                else:
                    ans.append('L')
                    L.append(num[numbers[j]])
    return ''.join(map(str,ans))    
