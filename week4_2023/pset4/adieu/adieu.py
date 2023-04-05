import inflect

p = inflect.engine()

def main():
    # Get user input
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

    for i in range(0,len(names)):
        say_goodnight(names[:i + 1])

def say_goodnight(list):
    names = str(p.join(list))
    print("Adieu, adieu, to", names)


if __name__ == "__main__":
    main()