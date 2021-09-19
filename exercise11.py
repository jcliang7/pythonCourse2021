# ships = ["electronics", 5, 2, 17, 29, 1, 1, 4]
ships = ["food", 11, 52, 190, 14, 73, 8, 391, 61, 215, 97, 10, 151, 15, 3]
goes = ['', 'Nankan', 'Zhongli', 'Taipei-Nei Hu', 'Taipei-Zhong He']
itemNeedSum = ['electronics', 'clothing', 'household']
itemNeedList = ['food', 'other']
total=0
print("This is a shipment of " + ships[0] + ".")
if (ships[0] in itemNeedSum):
    for idx in range(1, len(ships)-1):
        total += ships[idx]
    print("A total of " + str(total))
elif (ships[0] in itemNeedList):
    for idx in range(1, len(ships)-1):
        print("\t" + str(idx) + ": " + str(ships[idx]))
print(" products are going to " + goes[ships[-1]] + ".")
 