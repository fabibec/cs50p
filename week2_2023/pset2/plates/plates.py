def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    is_Valid = True
    length = len(s)
    index = 0

    for letter in s:
        if letter.isnumeric():
            break
        index += 1

    if length < 2 or length > 6:
        # Check for correct length
        is_Valid = False
    elif not s[0:2].isalpha() or not s.isalnum():
        # Checks if first two characters are letters and if the plate cotains any unallowed characters
        is_Valid = False
    elif index != length and s[index] == '0':
        # Check if first number is a zero
        is_Valid = False

    for letter in s[index:length]:
        # Check if there are letters occuring after the first number
        if letter.isalpha():
            is_Valid = False

    return is_Valid

main()
