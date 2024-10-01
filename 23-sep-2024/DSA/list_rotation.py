"""
given a rotated sorted list that was rotated some unknown
number of times, we need to find the minimum number of times it
was rotated.

input: A sorted rotated list
    e.g: [7, 9, 3, 5, 6]

output: Number of times the list is rotated
    e.g: 2
    
cases:
    - a list of size 10 rotated 3 times
    - a list of size 8 rotated 5 times
    - a list that wasn't rotated at all
    - a list that was rotated just once
    - a list that was rotated n-1 times, where n is the size of the list
    - a list that was rotated n times (get back the original list)
    - an empty list
    - a list containing just one element

binary-search:
    initilize left as 0 and right as length-1
    while left < right
        calculated the mid
        if mid == +
    
"""


tests = [
    {
        "nums": [45, 55, 60, 2, 7, 8, 9, 12, 23, 25, 34],
        "output": 3
    },
    {
        "nums": [8, 9, 12, 15, 17, 3, 4, 6],
        "output": 5
    },
    {
        "nums": [1, 2, 3, 4, 5, 6, 12],
        "output": 0
    },
    {
        "nums": [3, 9, 15, 18, 22, 31, 2],
        "output": 6
    },
    {
        "nums": [2, 3, 8, 12, 13, 19],
        "output": 0 # We are finding the minimum number of times so..
    },
    {
        "nums": [],
        "output": 0
    },
    {
        "nums": [1],
        "output": 0
    },
]

def evaluate_tests(function, tests):
    for i, t in enumerate(tests):
        res = function(t["nums"])
        print(f"test # {i}")
        print(f"input: {t["nums"]}")
        print(f"expected output: {t["output"]}")
        print(f"actual output: {res}")
        print(f"test: {"PASSED" if res==t["output"] else "FAILED"}")
        print("-"*20)
        print()


def bf_count_rotations(nums):
    """broute force solution"""
    if not nums:
        return 0
    
    smaller = nums[0]
    idx = 0
    for i in range(1, len(nums)):
        if nums[i] < smaller:
            smaller = nums[i]
            idx = i
    return idx


def count_rotations(nums):
    left, right = 0, len(nums)-1



# evaluate_tests(bf_count_rotations, tests)



import random

l = [
    [random.randint(10, 99) for _ in range(random.randint(3, 15))]
    for _ in range(random.randint(5,20))
]
def rotate(self, n):
    for i in range(n):
        ...
print(*l, sep="\n")
