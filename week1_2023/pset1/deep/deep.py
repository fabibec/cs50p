def main():
    answer = input("What's the answer to the Great Question of Life, the Universe and Everything? ").strip().lower().replace("-"," ")
    if answer == "42" or answer == "forty two":
        print("Yes")
    else:
        print("No")

main()