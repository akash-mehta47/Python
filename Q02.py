def power(x, y):
    if y == 0:
        return 1
    if y > 0:
        return x * power(x, y - 1)
    else:
        return 1 / power(x, -y)

x = int(input("Enter base (x): "))
y = int(input("Enter exponent (y): "))
print(f"{x}^{y} =", power(x, y))
