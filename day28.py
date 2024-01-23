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


def character():
  legend = input("Name your legend: ")
  characterType = input("Character type (Human, Elf, Wizard, Orc): ")
  return legend


repeat = "yes"
while repeat == "yes":
  print("Welcome to this character builder")
  character()
  print("Health: ", health())
  time.sleep(1)
  print("Strength:", strength())
  print()
  time.sleep(2)
  os.system("clear")
  print("Who are they battling? ")
  character()
  print("Health: ", health())
  time.sleep(1)
  print("Strength:", strength())
  print()
  time.sleep(2)
  os.system("clear")
  repeat = input("Would you like to create another character?")
else:
  exit()
