import sys


def main():
    filename = validate_input()
    
    try:
        ...
    except FileNotFoundError:
        sys.exit("Input does not exist")


def validate_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith((".jpg", ".jpeg", ".png")) or not sys.argv[2].endswith(
        (".jpg", ".jpeg", ".png")
    ):
        sys.exit("Invalid output")

    if sys.argv[1].split(".")[-1].lower() != sys.argv[2].split(".")[-1].lower():
        sys.exit("Input and output have different extensions")

    return sys.argv[1]


if __name__ == "__main__":
    main()
