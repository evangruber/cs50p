def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s[:2].isalpha() or not s.isalnum():
        return False

    digit_started = False

    for c in s[2:]:

        if c.isdigit():
            if not digit_started:
                digit_started = True

                if c == "0":
                    return False

        elif digit_started:
            return False

    return True


if __name__ == "__main__":
    main()
