def main():
    name = input("what's your name? ")
    print(hello(name))

def hello(name="world"):
    return f"hello, {name}"

if __name__ == "__main__":
    main()