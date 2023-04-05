def main():
    camelString = input("camelCase: ").strip()
    snake_string = ""
    for letter in camelString:
        if letter.isupper():
            snake_string += f"_{letter.lower()}"
        else:
            snake_string += letter
    print("snake_case: " + snake_string)

main()