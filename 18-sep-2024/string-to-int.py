def digit_to_int(digit):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(digits)):
        if digit == digits[i]:
            return i
    

def power(n, p):
    pow = 1
    for _ in range(p):
        pow *= n
    return pow

def multiple_of_10(digit, index, length):
    index = length-1-index
    return power(10, index) * digit

def string_to_int(string):
    digits = [d for d in string]
    converted_int = 0
    for i in range(len(string)):
        converted_int += multiple_of_10(digit_to_int(digits[i]), i, len(digits))
    return converted_int


string = "2231235223"
print(f"{string_to_int(string)=}")