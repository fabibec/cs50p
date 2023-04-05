def main():
    x = get_int("What's x? ")
    print(x)

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # print("x is not an integer!")
            pass

main()