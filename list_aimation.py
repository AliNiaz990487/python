import os
import time

array = 'M u h a m m a d U s m a n'.split()

def printRed(index):
    print(f'\033[01;31m{array[index]}\033[0m', end = ' ')
'''
\033[01;31m{array[index]}\033[0m
  1  2   3        4        5   6

1,5 -> they are escape sequences for anscii Standerd encoding
2   -> Print the character in bold(there are more styles as well <01, 03, 05, 07 ...>)
3   -> 31 is the actual red color for the character (30....39) different colors, I don't know the perpuse of (m) here but when we remove it, 
        |-> it hides the first character 
             |-> let us say we want to print khan
                  |-> with m  it will print ---> khan
                  |-> without m it will print ---> han
4   -> the character we want to print
5   -> see 1
6   -> back the color to normal (white), it can be \033[0;30m but that's shortcut
'''


'''
The basic principle here is the name has basicly three parts to be printed

M u h a m m a d U s m a n
w w w w r r r w w w w w w

the red parts is in between the white parts
    so we have used one loop for whites
    one for reds
    and another one for whites
'''
def printList(rightShift = 0, selected = 1):
    os.system('clear')
    rightMost = selected+rightShift

#-------------Handles the List index out of range issue------------------
    for i in range(1, selected):
        if(rightMost == len(array)+i):
            rightMost -= i

#-------------Printer loops------------------------------------
    for i in range(rightShift):
        print(array[i], end = ' ')
    for i in range(rightShift, rightMost):
        printRed(i)
    for i in range(rightMost, len(array)):
        print(array[i], end = ' ')
#-------------------------------------------------
    print()
        

# printList(rightShift=3, selected=4)
for i in range(3):  # number of times to animate
    for j in range(len(array)):
        printList(rightShift=j, selected=3)
        time.sleep(0.07)