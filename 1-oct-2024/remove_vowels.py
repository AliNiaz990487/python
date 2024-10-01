def remove_vowels(s):
    result = ''
    vowels = "aeiouAEIOU"
    
    for char in s:
        is_vowel = False
        for vowel in vowels:
            if char == vowel:
                is_vowel = True
                break
        if not is_vowel:
            result += char
    
    return result


s = "hello world"
print(remove_vowels(s))  # "hll wrld"
