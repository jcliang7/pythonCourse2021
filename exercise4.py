# Prompt the user with the text: "How much NT is this USD? "
running = True
while running:
    usd = input("How much NT is this USD? ")
    if (usd == "done"):
        running = False
    else:
        nt = str(int(usd)*30)
        print(usd + " USD is " + nt + " NT.")
print("Finish!")