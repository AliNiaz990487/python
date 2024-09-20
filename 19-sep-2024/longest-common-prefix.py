
def get_min(v1, v2):
    return v1 if v2>v1 else v2

def compare_strings(str1, str2):
    min_length = get_min(len(str1), len(str2))

    for i in range(min_length):
        if str1[i] < str2[i]:
            return True
        elif str1[i] > str2[i]:
            return False
    return len(str1) <= len(str2)


def sort_strings(strs):
    for i in range(len(strs)-1):
        for j in range(i+1, len(strs)):
            if compare_strings(strs[i], strs[j]):
                temp = strs[i]
                strs[i] = strs[j]
                strs[j] = temp


def longest_common_prefix(strs):
    if not strs:
        return "-1"

    sort_strings(strs)

    first = strs[0]
    last = strs[-1]
    min_length = get_min(len(first), len(last))
    i = 0
    while i < min_length and first[i] == last[i]:
        i += 1
    
    prefix = ""
    for j in range(i):
        prefix += first[j]

    return prefix
    


print(longest_common_prefix(
    ["torchvision", "torchtext", "torch", "torchaudio"]
))