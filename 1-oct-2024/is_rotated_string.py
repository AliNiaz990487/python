def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return False
    
    combined = s1 + s1 
    n = len(s2)
    
    for i in range(len(combined) - n + 1): 
        match = True
        for j in range(n):
            if combined[i + j] != s2[j]:
                match = False
                break
        if match:
            return True
    
    return False


s1 = "abcd"
s2 = "cdab"
print(are_rotations(s1, s2))  # True

s1 = "abcd"
s2 = "acdb"
print(are_rotations(s1, s2))  #False
