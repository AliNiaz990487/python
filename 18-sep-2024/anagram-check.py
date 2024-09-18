
def check_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    # same_char = list()

    exists = False
    for w1 in word1:
        for w2 in word2:
            if w1 == w2: 
                exists = True
        if not exists:
            return False
    
    return exists


print(f"{check_anagram("ten", "net")=}")
print(f"{check_anagram("seven", "evens")=}")
print(f"{check_anagram("ali", "boy")=}")