

def multiples_sum(upper_bound):
    s = 0
    for i in range(1, upper_bound):
        if i%3==0 or i%5==0:
            s += i
    return s    
    
print(f"{multiples_sum(1000)=}")