import os
import time

array = 'G u l A l a m K h a n'.split()

def printRed(index):
    print(f'\033[01;31m{array[index]}\033[0m', end = ' ')


def printList(numberOfSelection):
    os.system('clear')
    temp = numberOfSelection+4
    for i in range(1 , len(array)+4):
        if temp == len(array)+i:
            temp -= i

    for i in range(numberOfSelection):
        print(array[i], end = ' ')

    for i in range(numberOfSelection,temp):
        printRed(i)
    for i in range(temp, len(array)):
        print(array[i], end = ' ')
    print()
        

for j in range(len(array)):
    for i in range(len(array)+1):
        printList(i)
        time.sleep(0.1)