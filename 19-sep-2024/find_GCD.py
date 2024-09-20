def get_min(a, b):
    if a < b:
        return a
    return b


def get_GCD(a, b):
    minimum = get_min(a, b)
    for i in range(minimum, 1, -1):
        if a%i==0 and b%i==0: return i

a = 1080
b = 720

print(f"{get_GCD(a,b)=}")