def rotate_string(s, k):
    n = len(s)
    k = k % n 
    result = ""
    
    for i in range(n - k, n):  
        result += s[i]
    
    for i in range(n - k):  
        result += s[i]
    
    return result


s = "abcdef"
k = 2
print(rotate_string(s, k))  #"efabcd"
