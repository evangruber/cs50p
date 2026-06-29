import sys
import csv
from tabulate import tabulate


def main():
    filename = validate_input()

    table_contents = []

    try:
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            # Store the fieldnames in a list
            headers = reader.fieldnames
            # Store contents associated to each fieldname grouped as a list in a list
            for row in reader:
                table_contents.append([row[header] for header in headers])
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table_contents, headers, tablefmt="grid"))


def validate_input():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    return sys.argv[1]


if __name__ == "__main__":
    main()
