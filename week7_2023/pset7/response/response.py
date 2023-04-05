import validators

def main():
    if validate(input("What's your email address? ").strip()):
        print("Valid")
    else:
        print("Invalid")


def validate(s):
    return validators.email(s)


if __name__ == '__main__':
    main()