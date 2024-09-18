
def to_lower(char):
    capital_range = [ord('A'), ord('Z')]
    d = ord('a') - capital_range[0]
    ascii_char = ord(char)
    
    if ascii_char >= capital_range[0] and ascii_char <= capital_range[1]:
        return chr(ascii_char+d) # convert int to unicode string
    
    return char

def is_alphabet(char):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    char = to_lower(char)
    for a in alphabets:
        if char == a: return True
    
    return False

def is_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    char = to_lower(char)
    for v in vowels:
        if v == char: return True
    
    return False

def count_vowels_and_consunents(sentence):
    count = {"vowels": 0, "consunents": 0}
    for char in sentence:
        if not is_vowel(char) and not is_alphabet(char):
            continue
        if is_vowel(char):
            count["vowels"] += 1
            continue
        
        count["consunents"] += 1
            
        
    
    return count




sentence = "The quick bown fox / > jumped < ,over the lazy dog" # special characters are skiped

print(count_vowels_and_consunents(sentence))
