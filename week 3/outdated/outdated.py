def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:

        mid_endian_date = input("Date: ").strip()

        if "," in mid_endian_date:
            try:
                month, day, year = mid_endian_date.replace(",", "").split(" ")

                month = month.capitalize()

                if month not in months or not day.isdigit() or not 1 <= int(day) <= 31:
                    continue

                break
            except ValueError:
                continue

        if "/" in mid_endian_date:
            try:
                month, day, year = mid_endian_date.split("/")

                if int(month) > 12 or not 1 <= int(day) <= 31:
                    continue

                break
            except ValueError:
                continue

    if not month.isdigit():
        month = months.index(month) + 1

    print(f"{year}-{int(month):02}-{int(day):02}")


main()
