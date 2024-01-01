print("Fill in the blank lyrics!")
print("(Type in the blank lyrics and see if you are as cool as me.)")
count = 1
while True:
    print("Thank you for the happiest year of my ____.")
    answer = input("What is the missing word? ")
    if answer == "life" or answer == "Life":
      print("You are cool as me at", count, "attempts.")
      break
    else:
      print("Nice try, not yet as cool as me!")
      print("You have " + str(3 - count) + " guesses left.")
      count += 1
      if count > 3:
        print("Failed!")
        break
      
