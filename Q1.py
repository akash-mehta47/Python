num=int(input("Enter a positive integer: "))
if num<2:
    print(num,"is not prime")
else:
    for i in range(2,round(num**0.5)+1):
        if num%i==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")