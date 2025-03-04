import random

name = ("Sandi", "Maureen" , "Laureen")

names = input("Name to choose are Sandi, Maureen or Laureen: ")

if names in name:
    print("you win")
else:
    print("you lose")