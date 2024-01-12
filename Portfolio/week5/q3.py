#write a program to find 10 numbers from user your program should calculate arithmetic mean
#and arithmetic mean for those number
def input():
    numlist = []
    for i in range(10):
        number = float(input(f"Enter number {i+1}: "))
        numlist.append(number)
    return numlist

def calcu():
    leest = input()
    sum = 0
    product = 1

    for i in range(10):
        sum += leest[i]
        product *= leest[i]

    am = sum / len(leest)
    gm = product ** (1/len(leest))
    return am, gm

def outs():
    sum, product = calcu()
    print(f"The arithmetic mean is: {sum}")
    print(f"The geometric mean is: {product}")

outs()

