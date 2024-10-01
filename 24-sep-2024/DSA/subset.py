def subsets(arr):
    result = []
    
    def generate_subsets(i, current):
        if i == len(arr):
            result.append(current)
            return
        generate_subsets(i + 1, current)
        generate_subsets(i + 1, current + [arr[i]])
    
    generate_subsets(0, [])
    return result

arr = [1, 2, 3, 4, 5, 6]
print(subsets(arr)) 