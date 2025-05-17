num=int(input("Enter the number: "))
temp=1
i=1
while temp<=num:
    for j in range(i):
        if temp>num:
            break
        print(temp,end=" ")
        temp+=1
    print()
    i+=1