"""


1 
one 1 -> 11
two 1 -> 21
one 2 one 1 -> 1211
one 1 one 2 two 1 -> 111221
three 1 two 2 one 1 -> 312211
one 3 one 1 two 2 two 1 -> 13112221
one 1 one 3 two 1 three 2 one 1 -> 1113213211
three 1 one 3 one 2 one 1 one 3 one 2 two 1 -> 3113121113121
"""


def count_say(n):
    if n == 1: return "1"
    if n == 2: return "11"

    for i in range(3, n+1):
        prev = "11"
        next = ""
        for j in range(1, len(prev)): 
            _prev = prev[j-1]
            _next = prev[j]
            count = 0
            def count_repeated():
                nonlocal _prev, _next, j, count
                while _prev == _next and j < len(prev):
                    count += 1
                    j += 1
            count_repeated()
            next += f"{count}{prev[-1]}"
    
    return count

print(f"{count_say(4)=}")
