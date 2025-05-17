num=int(input("Enter a number: "))
temp=0
while num>0:
    temp+=num%10    
    num=num//10
print(temp)
    