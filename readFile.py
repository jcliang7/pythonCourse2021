book = open("textfile.txt", 'r')
chars = 0
for line in book:
    line = line.replace(' ', '')
    line = line.replace('\n', '')
    chars += len(line)
print(chars)
book.close()