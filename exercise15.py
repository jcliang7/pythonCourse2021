fileName = input("File name?")
print("***************************************")
book = open(fileName, 'r')
lines = 0
words = 0
chars = 0
for line in book:
    print(line)
    lines+=1
    wordlist = line.split(' ')
    words += len(wordlist)
    chars += len(line)

print(fileName, "contains ", lines, " lines, ", words, " words, and ", chars, " characters")
