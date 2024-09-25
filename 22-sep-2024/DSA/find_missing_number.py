

def missing_number(arr):
    n = len(arr)+1
    S = (n * (n+1)) // 2 # sum of natural numbers
    s = arr[0]
    for i in range(1, n-1):
        s += arr[i]
    return S-s


arr = [1, 2, 3, 5, 6, 7, 8, 9]
print(
    missing_number(arr)
)