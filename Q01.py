def prime_factor():
    while n % 2 == 0:
        max_prime = 2
        n //= 2
        
    i = 3
    while i * i <= n:
        while n % i == 0:
            max_prime = i
            n //= i
        i += 2

    if n > 2:
        max_prime = n

    return int(max_prime)

n = int(input("Enter a number: "))
print("Largest Prime Factor:", prime_factor(n))
