import sys
import csv


def main():
    filename = validate_input()
    fieldnames = []
    student_record = []

    try:
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)

            for field in reader.fieldnames:
                if field == "name":
                    fieldnames.extend(["first", "last"])
                else:
                    fieldnames.append(field)

            for row in reader:
                last_name, first_name = (
                    row[reader.fieldnames[0]].replace('"', "").split(",")
                )
                house = row[reader.fieldnames[1]]
                student_record.append(
                    {
                        "first": first_name.strip(),
                        "last": last_name.strip(),
                        "house": house,
                    }
                )

    except FileNotFoundError:
        sys.exit(f"Could not read {filename}")

    try:
        with open(sys.argv[2], "x") as new_csvfile:
            writer = csv.DictWriter(new_csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_record)
    except FileExistsError:
        pass


def validate_input():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    return sys.argv[1]


if __name__ == "__main__":
    main()
