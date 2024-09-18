

def is_rotated(string1, string2):
    first_half = ''
    for i in range(len(string1)//2):
        first_half += string1[i]
    second_half = ''
    for i in range(len(string1)//2, len(string1)):
        second_half += string1[i]
    
    rotated_string = second_half + first_half

    return rotated_string == string2




print(f"{is_rotated("abcdef", "defabc")=}")