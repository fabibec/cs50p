import random
import sys

def main():
    # Get level
    level = -1
    while level < 1:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass

    # Choose random integer
    number = random.randint(1,level)

    # Let the user guess
    while True:
        try:
            guess = int(input("Guess: "))
            evalute_guess(number,guess)
        except ValueError:
            pass

def evalute_guess(number,guess):
    if number == guess:
        sys.exit("Just right!")
    elif number < guess:
        print("Too large!")
    else:
        print("Too small!")

main()