def main():
    text = input("Input: ").strip()
    newtext = ""
    for letter in text:
        if letter.lower() not in ["a", "e", "i", "o", "u"]:
            newtext += letter
    print(newtext)

main()
