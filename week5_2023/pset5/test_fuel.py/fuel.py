def main():
    while True:
        percentage = convert(input("Input: "))
        if percentage != -1:
            print(gauge(percentage))
            break


def convert(fraction):
    fraction = fraction.strip()
    divider = fraction.find("/")
    x = fraction[:divider]
    y = fraction[divider + 1:]

    # Check for ValueError
    x = int(x)
    y = int(y)

    # Check for ZeroDivision Error
    fraction = x / y

    # Don't return illegal values
    if fraction <= 1:
        return round(fraction * 100)
    else:
        raise ValueError


def gauge(percentage):
    # Prints the correct output
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()