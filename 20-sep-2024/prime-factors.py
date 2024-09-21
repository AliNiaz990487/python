def largest_prime_factor(n):
    factors = []
    while n%2 == 0:
        factors.append(2)
        n//=2

    for i in range(3, int(n**0.5)+1, 2):
        while n%i==0:
            factors.append(i)
            n//=i

    if n > 2:
        factors.append(n)

    return factors[-1]


n = 600851475143
print(f"Prime factors of {n}: {largest_prime_factor(n)}")
