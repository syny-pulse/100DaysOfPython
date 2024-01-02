from getpass import getpass as input

player_1 = 0
player_2 = 0

while True:
    print("Hey, it's time to play Rocks, Scissors, and Paper! Let's begin!")
    choice_1 = input("Player 1, R, S or P? ")
    choice_2 = input("Player 2, R, S, P? ")

    if choice_1 == choice_2:
        print("It's a tie! \U0001F60A Yeah yeah, that's just the start, show me more!")

    else:
        if (
            (choice_1 == "R" and choice_2 == "S")
            or (choice_1 == "S" and choice_2 == "P")
            or (choice_1 == "P" and choice_2 == "R")
        ):
            print("Player 1 wins! \U0001F60E. Yoo this is it, this is it")
            player_1 += 1

        elif (
            (choice_1 == "S" and choice_2 == "R")
            or (choice_1 == "P" and choice_2 == "S")
            or (choice_1 == "R" and choice_2 == "P")
        ):
            print("Player 2 wins! Braaaaavo\U0001F60E")
            player_2 += 1

        else:
            print("Invalid input! \U0001F92F")
            break

    if player_1 == 3:
        print("Player 1 wins the game! \U0001F60E")
        break
    elif player_2 == 3:
        print("Player 2 wins the game! \U0001F60E")
        break
