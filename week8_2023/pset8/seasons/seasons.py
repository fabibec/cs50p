from datetime import datetime, date
import sys
import inflect

p = inflect.engine()

def main():
    birthdate = input("Date of Birth: ").strip()
    delta = date.today() - validate(birthdate)
    print(get_mins(delta))


def validate(date):
    try:
        return datetime.strptime(date, r"%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date")

def get_mins(delta):
    minutes = int(delta.total_seconds() / 60)
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"

if __name__ == "__main__":
    main()