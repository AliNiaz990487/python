def get_leaders(arr):
    n = len(arr)
    leaders = []
    for i in range(n-1):
        t = False
        for j in range(i+1, n):
            def check():
                nonlocal t
                if arr[j] > arr[i]:
                    t = True
            check()
            if t: break
        if not t:
            leaders.append(arr[i])

    leaders.append(arr[-1])
    print(leaders)
    return leaders        
            
            


arr = [16, 17, 4, 5, 3, 2]
get_leaders(arr)
