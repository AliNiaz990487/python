

def even_fib_sum(bound):
    a = 1
    b = 1
    s = 0
    while a<bound:
        if a%2 == 0:
            # print(end=f"{a}, ")
            s += a
        temp = b
        b = a+b
        a = temp

    return a

print(f"{even_fib_sum(4000000)=}")