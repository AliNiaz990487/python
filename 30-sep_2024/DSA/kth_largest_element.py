
def k_largest(arr, k):
    arr.sort(reverse=True) # sorted has already been done so builtin sort is used
    for i in range(k):
        print(arr[i], end=" ")



arr = [1, 23, 12, 9, 30, 2, 50]

k = 3
k_largest(arr, k)
