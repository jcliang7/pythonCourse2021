userCost_string = input("Please input a number between 1~1000:")
userCost = int(userCost_string)
if (userCost < 1 or userCost > 1000):
    print("Error!")
else:
    if userCost > 500:
        print("1000")
    elif userCost > 100:
        print("500")
    elif userCost > 50:
        print("100")
    elif userCost > 10:
        print("50")
    elif userCost > 5:
        print("10")
    else:
        print("5")
