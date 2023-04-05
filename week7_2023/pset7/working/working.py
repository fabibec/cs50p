import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matched := re.search(r"^((?:1[0-2]|[0-9])(?::(?:[0-5][0-9]))? (?:AM|PM)) to ((?:1[0-2]|[0-9])(?::(?:[0-5][0-9]))? (?:AM|PM))$", s, re.IGNORECASE):
        return f"{convert_time(matched.group(1))} to {convert_time(matched.group(2))}"
    raise ValueError

def convert_time(time):
    if time.find("AM") != -1:
        time = time.replace("AM","").strip()
        split_time = time.split(":")
        conversion_digit = int(split_time[0])
        if conversion_digit == 12:
            conversion_digit = 0
        return f"{str(conversion_digit).zfill(2)}:{split_time[1]}" if len(split_time) == 2 else f"{str(conversion_digit).zfill(2)}:00"
    elif time.find("PM") != -1:
        time = time.replace("PM","").strip()
        split_time = time.split(":")
        conversion_digit = int(split_time[0])
        if conversion_digit != 12:
            conversion_digit += 12
        return f"{str(conversion_digit).zfill(2)}:{split_time[1]}" if len(split_time) == 2 else f"{str(conversion_digit).zfill(2)}:00"
    raise ValueError

if __name__ == "__main__":
    main()