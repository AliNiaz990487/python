

def reverse(string):
    chars = [c for c in string]

    left = 0
    right = len(chars) - 1

    while left < right:
        temp = chars[left]
        chars[left] = chars[right]
        chars[right] = temp

        left += 1
        right -= 1

    return "".join(chars)

def is_palindrome(string):
    return string == reverse(string)


print(f"{is_palindrome("hello world")=}")
print(f"{is_palindrome("racecar")=}")