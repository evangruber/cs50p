def main():
    while True:
        try:
            x, y = (int(n) for n in input("Fraction: ").split("/"))

            if y == 0:
                raise ZeroDivisionError

            if x > y or x < 0:
                raise ValueError

            break

        except (ValueError, ZeroDivisionError):
            pass

    fuel_level = int(round((x / y) * 100))

    if fuel_level <= 1:
        print("E")
    elif fuel_level >= 99:
        print("F")
    else:
        print(f"{fuel_level}%")


main()
