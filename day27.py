import random
import os, time


def rollDice(sides):
  result = random.randint(1, sides)
  return result


def health():
  healthStat = ((rollDice(6) * rollDice(12)) / 2) + 10
  return healthStat


def strength():
  strengthStat = ((rollDice(6) * rollDice(8)) / 2) + 12
  return strengthStat


print("Welcome to this character builder")
repeat = "yes"
while repeat == "yes":
  legend = input("Name your legend: ")
  characterType = input("Character type (Human, Elf, Wizard, Orc): ")
  print()
  print("Health: ", health())
  time.sleep(1)
  print("Strength:", strength())
  print()
  time.sleep(4)
  os.system("clear")
  repeat = input("Would you like to create another character?")
else:
  exit()
