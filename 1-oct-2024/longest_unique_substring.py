def longest_unique_substring(s):
    start = 0
    max_length = 0
    seen = {}
    
    for end in range(len(s)):
        current_char = s[end]

        if current_char in seen:
            start = max(start, seen[current_char] + 1)
        
        seen[current_char] = end  
        max_length = max(max_length, end - start + 1)
    
    return max_length

s = "abcabcbb"
print(longest_unique_substring(s))  # 3 ("abc")
