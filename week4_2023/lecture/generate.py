# Importing the whole module
# import random
from random import choice, randint, shuffle

coin = choice(["heads", "tails"])
print(coin)

number = randint(1, 10)
print(number)

cards = ["jack","queen","king"]
shuffle(cards)
print(cards)