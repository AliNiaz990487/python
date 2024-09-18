def reverse(string):
    chars = [c for c in string]
    reversed_string = str()
    for i in range(len(chars)-1, -1, -1):
        reversed_string += chars[i]
    
    return reversed_string


def reverse_in_place(string):
    chars = [c for c in string]
    left = 0
    right = len(chars) - 1
    while left < right:
        temp = chars[left]
        chars[left] = chars[right]
        chars[right] = temp

        left += 1
        right -= 1

    return ''.join(chars)


print(reverse("hello world"))
print(reverse_in_place("hello world"))



