
def compress_string(string):
    if len(string) < 2:
        return string
    
    final_string = ""
    i = 1

    def repeating_char(prev_char):
        nonlocal i
        count = 1
        while i < len(string) and string[i] == prev_char:
            count += 1
            i += 1
        return count 
    
    while i < len(string):
        prev_char = string[i-1]
        count = repeating_char(prev_char)
        i += 1
        final_string += f"{prev_char}{count}"

    return final_string




string = "aaabbccxxxyyzzzgggggggg"
print(compress_string(string))