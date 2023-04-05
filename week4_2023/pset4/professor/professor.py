import random

def main():
    score = 0
    level = get_level()
    for _ in range(10):
        score += ask_question(level)

    print("Score:",score)


def get_level():
    # Get level from user
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    # Raise error for wrong value
    if level not in [1, 2, 3]:
        raise ValueError

    # Create integer, 0 as low for level 1
    if level == 1:
        low = 0
    else:
        low = 10 ** level / 10
    high = 10 ** level - 1
    
    return random.randint(low,high)


def ask_question(level):
    # Generate Question and Answer
    x = generate_integer(level)
    y = generate_integer(level)
    answer = x + y

    for _ in range(3):
        # Get user inpt & output EEE for invalid input
        try:
            user_answer = int(input(f"{x} + {y} = "))
        except ValueError:
            print("EEE")
            continue

        # Increase score by one for right answer else print EEE
        if user_answer == answer:
            return 1
        else:
            print("EEE")

    # If the user didn't find the answer after 3 trys print the correct answer
    print(f"{x} + {y} = {answer}")
    return 0

if __name__ == "__main__":
    main()