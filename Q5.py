a,b=map(int,input("Enter two numbers: ").split())

temp = max(a,b)

while True:
    if temp % a == 0 and temp % b == 0:
        print("LCM is:",temp)
        break
    temp +=1