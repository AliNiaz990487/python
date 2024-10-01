"""
We need to write a program to find the position of a given number
in a list arranged in decreasing order, we also need to to minimize the number
of times the access of the element form the list.


input: 
    cards = [13, 12, 11, 7, 4, 3, 1, 0]
    query = 7
output:
    the position of the query (i.e index -> 3)

test cases:
    - the query occurs in the middle
    - the query is the last element
    - the query is the first element
    - the list has just one element
    - the list doesn't contains query
    - the list is empty
    - the number query occurs at more than one place
"""

tests = [
    {
        "input": {
            "cards": [13, 11, 10, 7, 4, 3, 1, 0],
            "query": 7
        },"output": 3
    },{
        "input": {
            "cards": [13, 11, 10, 7, 4, 3, 1, 0],
            "query": 0
        }, "output": 7
    },{
        "input": {
            "cards": [13, 11, 10, 7, 4, 3, 1, 0],
            "query": 13
        }, "output": 0
    },{
        "input": {
            "cards": [10],
            "query": 10
        }, "output": 0
    },{
        "input": {
            "cards": [13, 11, 10, 7, 4, 3, 1, 0],
            "query": 20
        }, "output": -1
    },{
        "input": {
            "cards": [],
            "query": 10
        }, "output": -1
    },{
        "input": {
            "cards": [6, 6, 2, 2, 2, 1, 1, 1, 0],
            "query": 2
        }, "output": 2
    }
]

def unit_test(func, tests):
    for i, t in enumerate(tests):
        res = func(**t['input'])
        print(f"\033[1;mTest # {i}\033[0m")
        print(f"inputs: {t["input"]}")
        print(f"expacted output: {t["output"]}")
        print(f"actual output: {res}")

        if res == t['output']:
            print(f"result: \033[1;32m PASSED\033[0m")
        else:
            print(f"result: \033[1;31mFAILED\033[0m")
        print("-"*10)

def bf_predict_card(cards, query):
    """brute force prediction"""
    for i in range(len(cards)):
        if cards[i] == query:
            return i

    return -1

def test_location(cards, query, mid):
    if query == cards[mid]:
        if mid-1 >= 0 and query == cards[mid-1]:
            return "left"
        return "found"
    if query > cards[mid]:
        return "left"
    return "right"
    

def predict_card(cards, query):
    """optimized prediction"""
    left, right = 0, len(cards)-1


    while left <= right:
        mid = (left+right) // 2
        result = test_location(cards, query, mid)
        # print(f"{left=} {right=} {mid=} {query=}")
        if result == "found":
            return mid
        if result == "left":
            right = mid-1
        else:
            left = mid+1

    return -1


unit_test(predict_card, *[tests])
