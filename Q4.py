num=input("Enter a number: ")
for i in range(0, len(num)//2):
    if num[i] != num[len(num)-i-1]:
        print("Number is not palindrome")
else:
    print("Palindrome")