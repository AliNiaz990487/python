def iterative_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(iterative_fibonacci(6))
print(fibonacci(6))  # 8
