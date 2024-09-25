def pivoted_search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] >= arr[low]:
            if key >= arr[low] and key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if key > arr[mid] and key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1 


arr1 = [4, 5, 6, 7, 0, 1, 2]
key1 = 0
result1 = pivoted_search(arr1, key1)
print(result1)  

arr2 = [4, 5, 6, 7, 0, 1, 2]
key2 = 3
result2 = pivoted_search(arr2, key2)
print(result2)  
