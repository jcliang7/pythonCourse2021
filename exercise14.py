import random
ans = random.randint(1, 10)
cnt = 1
guess = int(input("What's your guess? "))
while guess != ans:
    if (guess < ans):
        print("Too low!")
    else:
        print("Too high!")
    cnt+=1
    guess = int(input("What's your guess? "))
if cnt == 1:
    print("Wow! You got it at first try.")
else:
    print("You got it!")
    print("And it only took you", cnt, "tries!")