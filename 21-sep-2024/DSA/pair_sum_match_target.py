

def naive_pair_sum(arr, target):  # O(n**2)
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i]+arr[j] == target: return True

    return False


def selection_sort(arr, reverse = False):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if (arr[i]>arr[j] and not reverse) or (arr[i]<arr[j] and reverse):
                arr[i], arr[j] = arr[j], arr[i]
    

def binary_search(arr, left, right, target):
    while (left <= right):
        mid = (left + right) // 2

        if arr[mid] == target: return mid

        if target > arr[mid]:
            left = mid+1
        else:
            right = mid-1


def pair_sum(arr, target):
    selection_sort(arr)
    left = 0
    right = len(arr)-1
    while left <= right:
        s = arr[left] + arr[right]
        if s == target: return True

        if s > target: 
            right -= 1
        else: 
            left += 1

    return False
arr = [0, -1, 2, -3, 1]
target = 5
# print(f"{naive_pair_sum(arr, target)=}")
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(binary_search(arr, 0, len(arr), 1))

# selection_sort(arr)
print(
    pair_sum(arr, 1)
)