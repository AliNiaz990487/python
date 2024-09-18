

def is_digit(char):
    return char >= "0" and char <= "9"

    
def expand_string(string):
    final_string = ""
    for i in range(len(string)):
        if is_digit(string[i]):
            prev_char = string[i-1]
            count = int(string[i])
            for _ in range(count):
                final_string += prev_char

    return final_string



print(f"{expand_string("a2x5y1q2")=}")