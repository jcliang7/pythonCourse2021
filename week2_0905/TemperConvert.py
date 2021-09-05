# Temperature Converter (F to C)
print("***************************************************************************")
print("Temperature Converter")
print("This program will convert Fahrenheit to Celsitus!\n\n")

f_string = input('Please enter the Fahrenheit value that you wish to convert: ')
f_float = float(f_string)
c_float = (f_float-32)*5/9
c_string = str(c_float)
print(f_string, " degrees Fahreheit is equal to " , c_string, " degrees Celsius.")
# print(f_string + " degrees Fahreheit is equal to " + c_string + " degrees Celsius.")
print("***************************************************************************")