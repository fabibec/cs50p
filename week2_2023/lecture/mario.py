def main():
    print_square(4)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(height):
    print("?" * height)

def print_square(height):
    for i in range(height):
        for j in range(height):
            print("#", end="")
        print()

main()