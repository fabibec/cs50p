import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matched := re.search(r"<iframe.*src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\".*></iframe>", s, re.IGNORECASE):
        # If found strip link ending and build the shorter link
        return f"https://youtu.be/{matched.group(1)}"
    return None

if __name__ == "__main__":
    main()