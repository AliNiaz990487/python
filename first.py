def myRange(start, end):
    arr = []
    while start != end:
        arr.append(start)
        start += 1
    return arr
print('[',"\033[31m", end='')
for i in myRange(0, 10):
    if i == 9: print(i, end='')
    else: print(i, end=', ')
print('\033[0m]')

