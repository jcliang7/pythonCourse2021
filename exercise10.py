list1 = [3, 5, 15]
list2 = [2, 1, 6]
total=0
for idx in range(len(list1)):
    total += ((list1[idx]-list2[idx])**2)
print(total)