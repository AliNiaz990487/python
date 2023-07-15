import time

# a < b < c
# a**2 + b**2 = c**2
# a + b + c = 1000

#---Initial Case
a = 3
b = 4
c = 5

def validateTriplate(a, b, c):
    return a**2 + b**2 == c**2

def generateTriplate():
    global a,b,c
    i = 3
    while(a+b+c != 1000):
        if(validateTriplate(a*i, b*i, c*i)):
            a = a*i
            b = b*i
            c = c*i
            print(f"|{i}| a({a}) = {a*i} | b({b}) = {b*i} | c({c}) = {c*i}")
            time.sleep(1)
        i += 1


generateTriplate()
# print(validateTriplate())
