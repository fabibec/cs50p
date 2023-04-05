import sys
import os
from PIL import Image, ImageOps

def main():
    # Validate command-line arguments
    l = len(sys.argv)
    if l > 3:
        sys.exit("Too many command-line arguments")
    elif l < 3:
        sys.exit("Too few command-line arguments")

    # Collect extensions
    second_extension = os.path.splitext(sys.argv[2])[1].lower()
    first_extension = os.path.splitext(sys.argv[1])[1].lower()
    print(first_extension, second_extension)
    if first_extension != second_extension:
        sys.exit("Input and output have different extension")
    elif not first_extension in [".jpg", ".jpeg", ".png"] or not second_extension in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")

    # Image manipulation
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("The file shirt.png could not be opend")

    size = shirt.size

    try:
        im = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"The file {sys.argv[1]} could not be opend")

    im = ImageOps.fit(im, size)
    im.paste(shirt, shirt)

    im.save(sys.argv[2])

    im.close()
    shirt.close()

if __name__  == "__main__":
    main()



