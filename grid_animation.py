import os

length = 25

data = [i for i in range(length)]

def printRed(index):
    print(f'\033[01;31m{data[index]}\033[0m', end = ' ')

def printGrid(red):
    temp = False
    for row in range(length//5):
        for col in range(5):
            if not temp:
                for k in range(red, 2):
                    printRed((row*5)+k)
                    temp = True
            if temp:
                continue
            print(data[(row*5)+col], end = ' ')
        print()

printGrid(0)
