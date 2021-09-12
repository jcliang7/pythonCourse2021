# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
numbers = []
cnt = 0
print("Pleanse input 10 numbers")
while cnt < 10:
    num_str = input()
    if num_str.isalnum():
        numbers.append(int(num_str))
        cnt+=1
    else:
        print("Not num.")
evenNum = 0
oddNum = 0
for n in numbers:
    if n % 2 == 0:
        evenNum += 1
    else:
        oddNum += 1
print("Number of enven numbers : " + str(evenNum))
print("Number of odd numbers : " + str(oddNum))