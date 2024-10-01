"""
a list consist of duplicate elements in decending order,
we need to find the starting and ending location (index) of
a particular element.

input: 
    repeating_numbers: [8, 8, 4, 4, 4, 4, 2, 0, -1]
    query: 4
output: (2, 5)

cases:
    - there is no repeating number
    - there is a repeating number
    - the repeating number index starts from 0
    - the whole list is repeating
    - there is no element in the list
    - there is only one element in the list
    - the query doesn't exists in the list
"""

tests = [
    {
        "input": {
            "repeating_numbers": [8, 7, 5, 4, 3, 2, 1, 0],
            "query": 5,
        }, "output": (2, 2)
    },
    {
        "input": {
            "repeating_numbers": [8, 8, 4, 4, 4, 4, 2, 0, -1],
            "query": 4,
        }, "output": (2, 5)
    },
    {
        "input": {
            "repeating_numbers": [8, 8, 8, 8, 2, 1, 0, -4],
            "query": 8,
        }, "output": (0, 3)
    },
    {
        "input": {
            "repeating_numbers": [4, 4, 4, 4, 4, 4, 4],
            "query": 4,
        }, "output": (0, 6)
    },
    {
        "input": {
            "repeating_numbers": [],
            "query": 3,
        }, "output": (-1, -1)
    },
    {
        "input": {
            "repeating_numbers": [3],
            "query": 3,
        }, "output": (0, 0)
    },
    {
        "input": {
            "repeating_numbers": [3, 2, 1, 0, -12],
            "query": 5,
        }, "output": (-1, -1)
    } 
]

def unit_test(function, tests):
    for i, t in enumerate(tests):
        res = function(**t["input"])
        print(f"Test # {i}")
        print(f"input: {t["input"]}")
        print(f"expected output: {t['output']}")
        print(f"actual output: {res}")
        if res == t['output']:
            print(f"test: \033[1;32mPASSED ✓\033[0m")
        else: 
            print(f"test: \033[1;31mFAILED ✕\033[0m")
        print("-"*20)


def bf_start_and_end_location(repeating_numbers, query):
    """broute force find repeated location"""
    if not repeating_numbers:
        return (-1, -1)
    if len(repeating_numbers) == 1:
        return (0, 0)
    
    start, end = -1, -1

    for i in range(1, len(repeating_numbers)):
        if repeating_numbers[i-1] != query:
            continue

        if start == -1 or end == -1:
            start = i-1
            end = i-1
        if repeating_numbers[i] == query:
            end = i

    return (start, end)


def start_location(repeating_numbers, query):
    left, right = 0, len(repeating_numbers)-1
    
    def test_location(mid):
        if query == repeating_numbers[mid]:
            if mid > 0 and repeating_numbers[mid-1]==query:
                return "left"
            return "found"
        if query > repeating_numbers[mid]:
            return "left"
        return "right"

    while left <= right: 
        mid = (left+right) // 2
        result = test_location(mid)
        if result == "found":
            return mid
        
        if result=="left":
            right = mid-1
        else: 
            left = mid+1

    return -1

def end_location(repeating_numbers, query):
    left, right = 0, len(repeating_numbers)-1

    def test_location(mid):
        if query == repeating_numbers[mid]:
            if mid < len(repeating_numbers)-1 and query == repeating_numbers[mid+1]:
                return "right"
            return "found"
        if query < repeating_numbers[mid]:
            return "right"
        return "left"
    
    while left <= right:
        mid = (left+right) // 2
        result = test_location(mid)

        if result == "found":
            return mid
        if result == "right":
            left = mid+1
        else:
            right = mid-1

    return -1


def start_and_end_location(repeating_numbers, query):
    return start_location(repeating_numbers, query), end_location(repeating_numbers, query)

unit_test(start_and_end_location, tests)
# unit_test(bf_repeated_location, [tests[0]])