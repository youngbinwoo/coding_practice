num=int(input())
s=0
for i in range(1,num+1):
    a=num//i
    s+=i*a
print(s)
