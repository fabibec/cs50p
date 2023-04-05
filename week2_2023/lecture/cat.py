# Loops
def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

# While
i = 0
while i < 3:
    print("meow")
    i += 1

# range: 0,1,2
for _ in range(3):
    print("meow")

print("meow" * 3, end="")


while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")