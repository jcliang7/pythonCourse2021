# number = 1

# while number <= 10:
#     print(number)
#     number+=1
# print("Done!")
#============================
# More loop stuff
# var = 1
# while var==1:
#     num = input("Enter a number:(input \"done\" to exit.)\n")
#     if (num == "done"):
#         var = 2
#     else:
#         print("You entered:" + str(num))
# print("Good bye!")
#===============================
# Password Example
password = ""
maxTries = 5
tries = 0
while password != "secret" and tries < maxTries:
    password = input("Please enter the password:")
    tries += 1
    if password == "secret":
        print("You have entered the correct password.")
    elif tries == maxTries:
        print("Incorrect password " + str(maxTries) + " times in a row.Please train again in 3 minutes.")
    else:
        print("Sorry, the password is incorrect - try again.")