
def is_divisble(n, start, end):
    for i in range(start, end+1):
        if n%i != 0:
            return False
    return True



def smallest_multiple():
    n = 1
    while not is_divisble(n, 1, 20):
        print(end=f"{n}    \r")
        n+=1
    return n

print(
smallest_multiple()
)