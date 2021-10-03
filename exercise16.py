number_as_text = input('Strating number? ')
number = int(number_as_text)
cnt = 0
# Open a file called output.txt for writing.
outputFile = open("output.txt", 'w')
while number != 1:
    if number % 2 == 0:
         number = number // 2
    else:
        number = 3*number + 1
    print(number)
# write the number to the file.
    cnt += 1
    ans = str(cnt) + ": " + str(number) + "\n" 
    outputFile.write(ans)
outputFile.close()