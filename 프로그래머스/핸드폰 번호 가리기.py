def solution(phone_number):
    ans=''
    for i in range(len(phone_number)-4):
        ans+='*'
    for i in range(len(phone_number)-4,len(phone_number)):
        ans+=phone_number[i]
    return ans
