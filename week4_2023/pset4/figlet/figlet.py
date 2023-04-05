from pyfiglet import Figlet
import sys
import random

def main():
    # Check usage
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid usage")

    figlet = Figlet()

    # Set Font
    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(figlet.getFonts()))
    else:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")

    # Prompt for text and print formatted result
    text = input("Input: ").strip()
    print("Output:")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()

