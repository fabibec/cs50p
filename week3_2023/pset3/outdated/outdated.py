def main():
    while True:
        date = format_date(input("Date: ").strip().title())
        if date != -1:
            print(date)
            break

def format_date(date):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    formatted_date = ""

    if date.find("/") != -1:
        # handle 9/8/1636
        date = date.split("/")
        try:
            formatted_date = date[2] + f"-{int(date[0]):02}-{int(date[1]):02}"
        except (IndexError, ValueError):
            return -1
    else:
        # Handle September 8, 1636
        month = 1
        for m in months:
            if date.find(m) == 0:
                break
            else:
                month += 1
        if month == 13:
            return -1
        try:
            year = date.split(",")[1].strip()
            day = date.split(",")[0].split(" ")[1]
            formatted_date = year + f"-{int(month):02}-{int(day):02}"
        except IndexError:
            return -1

    # Check for correct dates
    check = formatted_date.split("-")
    if int(check[1]) > 13 or int(check[2]) > 31:
        return -1

    return formatted_date

main()