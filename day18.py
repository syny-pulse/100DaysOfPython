print("Hello, Welcome to my game.")
print("Guess a number between 0 and 1,000,000")
myNum = 489767
tries = 0
while True:
    yourGuess = int(input("Enter your guess: "))
    if yourGuess > myNum:
        print("Your guess is too high.")
        tries += 1
        continue
    elif yourGuess < myNum and yourGuess > 0:
        print("Your guess is too low.")
        tries += 1
        continue
    elif yourGuess == myNum:
        tries += 1
        print("You win at",tries)
        break
    elif yourGuess < 0:
        exit()
