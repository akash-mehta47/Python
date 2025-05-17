num=int(input("Enter the number of rows: "))
temp=1
for i in range(num):
    for j in range(num):
        if i==j or i+j == num-1:
            print("0 ",end=" ")
        else:
            print(temp,end=" ")
            temp+=1
    print()