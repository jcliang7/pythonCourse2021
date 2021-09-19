def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

def exponent(a, x):
    return a**x

def squareRoot(number):
    if number < 0.0:
        print('Number must be positive!')
        exit()
    elif number < 1.0:
        lower = number
        upper = 1.0
    else:
        lower = 1.0
        upper = number

    i = 0
    while i < 100:
        middle = (lower + upper)/2
        if middle ** 2 < number:
            lower = middle
        else:
            upper = middle
        i += 1
    return upper