import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^(?:\d{1,3}\.){3}\d{1,3}$", ip):
        bytes = ip.split(".")
        for b in bytes:
            if int(b) > 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()