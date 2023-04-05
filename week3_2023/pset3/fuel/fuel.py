def main():
    while True:
        percentage = get_input()
        if percentage != -1:
            print_percentage(percentage)
            break

def get_input():
    # Get input and split it into two variables
    z = input("Fraction: ").strip()
    divider = z.find("/")
    x = z[:divider]
    y = z[divider + 1:]

    # Check for ValueError
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return -1

    # Check for ZeroDivision Error
    try:
        z = x / y
    except ZeroDivisionError:
        return -1

    # Don't return illegal values
    return z if z <= 1 else -1

def print_percentage(value):
    # Prints the correct output
    value = round(value * 100)
    if value >= 99:
        print("F")
    elif value <= 1:
        print("E")
    else:
        print(f"{value}%")


main()