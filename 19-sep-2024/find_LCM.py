def get_min(a, b):
    return a if a<b else b

def get_HCF(a, b):
    min_n = get_min(a, b)
    for i in range(min_n//2, 1, -1):
        if a%i==0 and b%i==0: return a
    

def get_LCM(a, b):
    return (a*b)//get_HCF(a,b)
    
a, b = 6, 15
print(f"{get_LCM(a,b)=}")