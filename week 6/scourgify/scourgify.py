import sys
import csv


def main():
    filename = validate_input()
    student_record = {}
    header = False

    try:
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                last_name, first_name = (
                    row[reader.fieldnames[0]].replace('\"', "").split(",")
                )
                with open(sys.argv[2], "w", newline="") as new_csvfile:
                    writer = csv.DictWriter(
                        new_csvfile, fieldnames=["first", "last", reader.fieldnames[1]]
                    )
                    if not header:
                        writer.writeheader()
                        header = True
                    writer.writerow(
                        {
                            "first": first_name.strip(),
                            "last": last_name.strip(),
                            f"{reader.fieldnames[1]}": row[reader.fieldnames[1]].strip(),
                        }
                    )
    except FileNotFoundError:
        sys.exit(f"Could not read {filename}")


def validate_input():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    return sys.argv[1]


if __name__ == "__main__":
    main()
