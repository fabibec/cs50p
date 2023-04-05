def main():
    expression = input("Expression: ").strip().split(" ")
    x = float(expression[0])
    z = float(expression[2])
    match expression[1]:
        case "+":
            print(x + z)
        case "-":
            print(x - z)
        case "*":
            print(x * z)
        case "/":
            if z != 0:
                print(x / z)
            else:
                print("Division through zero is not possible!")
        case _:
            print("Could not read expression")

main()
