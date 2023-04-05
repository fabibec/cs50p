def main():
    text = input("Input: ").strip()
    print(shorten(text))


def shorten(word):
    newtext = ""
    for letter in word:
        if letter.lower() not in ["a", "e", "i", "o", "u"]:
            newtext += letter
    return newtext


if __name__ == "__main__":
    main()