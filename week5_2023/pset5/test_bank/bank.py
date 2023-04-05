def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting[0:1] == "h":
        if greeting[0:5] == "hello":
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()