while True:
    try:
        num=int(input("Enter a number: "))
        if num>0:
            print(f"{num} is valid ")
            break
        else:
            print("Enter a positive integer")
    except:
        print("Invalid input")