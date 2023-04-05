def main():
    greeting = input("Greeting: ").strip().lower()
    if greeting[0:1] == "h":
        if greeting[0:5] == "hello":
            print("$0")
        else:
            print("$20")
    else:
        print("$100")

main()