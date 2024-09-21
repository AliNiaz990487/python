
def occur_odd_times(arr):
    n = len(arr)
    for i in range(n-1):
        count = 0
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                count += 1

        if count%2 != 0:
            elm = arr[i]

    print(elm, count)





arr = [1, 2, 3, 2, 3, 1, 3]
occur_odd_times(arr)