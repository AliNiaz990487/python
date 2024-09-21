
def naive_mejority(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        c = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                c += 1
        if count <= c:
            count = c
            elem = arr[i]

    print(elem, count)

arr = [1, 1, 2,2, 2,2, 1, 3, 5, 1]
naive_mejority(arr)