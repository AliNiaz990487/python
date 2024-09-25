
def naive1_max_sub_array(arr): #O(n**3)
    n = len(arr)
    S = 0
    for i in range(n):
        for j in range(i, n):
            s = arr[i]
            for k in range(i+1, j+1):
                s += arr[k]
        if s > S:
            S = s
        
    print(S)

def naive2_max_sub_array(arr): #O(n**2)
    n = len(arr)
    S = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
        
        if s > S:
            S = s

    print(S)


def kadanes_algo(arr): # O(n)
    n = len(arr)
    t_mx = 0
    mx = 0
    for i in range(n):
        t_mx += arr[i]
        if t_mx > mx:
            mx = t_mx
        if t_mx < 0:
            t_mx = 0

    print(mx)

arr = [2, 3, -8, 7, -1, 2, 3]
naive1_max_sub_array(arr)
naive2_max_sub_array(arr)
kadanes_algo(arr)