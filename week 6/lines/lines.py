import sys


def main():

    filename = validate_input()

    try:
        with open(filename, "r") as file:
            code_lines = [
                line
                for line in file
                if not line.lstrip().startswith("#") and line.strip()
            ]
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(len(code_lines))


def validate_input():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    return sys.argv[1]


if __name__ == "__main__":
    main()
