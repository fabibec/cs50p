def main():
    time = convert(input("What time ist it? ").strip())
    if between(7, 8, time):
        print("breakfast time")
    elif between(12, 13, time):
        print("lunch time")
    elif between(18, 19, time):
        print("dinner time")


def convert(time):
    time = time.replace(":",".")

    # Convert .pm
    if time.find(" p.m.") != -1:
        time = float(time.replace(" p.m.","")) + 12
    else:
        # Cut out .am ending
        time = float(time.replace(" a.m.",""))

    # Convert minutes
    minutes = round(time % 1 * 1.666,2)
    time = round(time) + minutes
    return time

def between(low,high,num):
    return num >= low and num <= high

if __name__ == "__main__":
    main()