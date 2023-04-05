balance = 0


def main():
    print("Balance:", balance)
    desposit(100)
    withdraw(50)
    print("Balance:", balance)

def desposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()