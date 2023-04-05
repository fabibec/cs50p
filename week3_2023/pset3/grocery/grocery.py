def main():
    dict = {}
    while True:
        try:
            text = get_input()
            try:
                dict[text] += 1
            except KeyError:
                dict[text] = 1
        except EOFError:

            print_dict(dict)
            break

def get_input():
    return input().strip().upper()

def print_dict(list):
    for key in sorted(list):
        print(list[key], key)

main()