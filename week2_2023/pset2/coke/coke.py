def main():
    owed = 50

    while owed > 0:
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25, 50]:
            owed -= coin
        if owed > 0:
            print(f"Amount Due: {owed}")
        else:
            print(f"Change Owed: {owed * (-1)}")

main()