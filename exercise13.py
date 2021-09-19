import exercise13utils

print("Please select the following")
functionText = input("add, subtract, multiply, divide, square root, exponent (choose one):").lower()

if functionText == "add":
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    print(exercise13utils.add(num1, num2))

elif functionText == "subtract":
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    print(exercise13utils.subtract(num1, num2))

elif functionText == "multiply":
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    print(exercise13utils.multiply(num1, num2))

elif functionText == "divide":
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    print(exercise13utils.divide(num1, num2))

elif functionText == "exponent":
    num1 = float(input("A^x\n Please enter A (base number): "))
    num2 = float(input("Please enter x (the exponent): "))
    print(exercise13utils.exponent(num1, num2))

elif functionText == "square root":
    num1 = float(input("Please enter the number you wish to find the square root of: "))
    
    print(exercise13utils.squareRoot(num1))