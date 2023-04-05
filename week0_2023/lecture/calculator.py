def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def old_calculator():
    # input always returns a string
    x = float(input("What's x? "))
    y = float(input("What's y? "))

    # round number to nearest int
    z = round(x + y)

    # print number formated with comas
    print(f"{z:,}")

    # round with f-string
    # print(f"{z:.2f}")

def square(n):
    return n**2

main()