def remove_duplicates(s):
    seen = {}
    result = ''
    
    for char in s:
        if char not in seen:
            seen[char] = True
            result += char
    
    return result

s = "programming"
print(remove_duplicates(s))  # "progamin"
