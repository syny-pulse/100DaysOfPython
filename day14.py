from getpass import getpass as input

print("Hey, its time to play Rocks, Scissors and Paper! Lets begin!")
player_1 = input("Player 1, R, S or P? ")
player_2 = input("Player 2, R, S, P? ")
if player_1 == player_2:
    print(
        "Its a tie! \U0001F60A Yeah yeah, thats just the start, show me more!")
else:
    if player_1 == "R" and player_2 == "S" or player_1 == "S" and player_2 == "P" or player_1 == "P" and player_2 == "R":
        print("Player 1 wins! \U0001F60E. Yoo this is it, this is it")
    elif player_1 == "S" and player_2 == "R" or player_1 == "P" and player_2 == "S" or player_1 == "R" and player_2 == "P":
        print("Player 2 wins! Braaaaavo\U0001F60E")
    else:
        print("Invalid input! \U0001F92F")
