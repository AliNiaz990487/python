
def is_palindrome(n):
    return f"{n}" == f"{n}"[::-1]

def largest_palindrome_product():
    largest = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            mul = i*j
            if is_palindrome(mul) and mul > largest:
                print(i, j)
                largest = mul
    return largest
            



print(f"{largest_palindrome_product()=}")