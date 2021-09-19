text = input('Number?')

number = float(text)
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
    # print(str(i) + ": " + str(lower) + ", " + str(upper))
    print(str(i) + ":" + str(lower) + ", " + str(upper))
    middle = (lower + upper)/2
    if middle ** 2 < number:
        lower = middle
    else:
        upper = middle
    i += 1

print(upper)