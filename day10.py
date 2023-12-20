myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = float(input("What percentage do you want to tip?: "))
tip = tip / 100
totalBill = myBill + (myBill * tip)
answer = totalBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)
