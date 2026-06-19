def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # [x] plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    # [x] plates must start with at least two letters.
    # [x] Numbers cannot be used in the middle of a plate; they must come at the end.
    # [x] first number used cannot be a ‘0’.
    # [x] No periods, spaces, or punctuation marks are allowed.

    if 2 > len(s) or len(s) > 6:
        return False
    elif len(s) == 2 and s.isalpha():
        return True
    elif not s[:2].isalpha() or not s.isalnum():
        return False
    elif s.isalpha():
        return True
    else:
        return check_num(s)


def check_num(plate_num):
    numbers = []
    digits_found = 0

    for i, c in enumerate(plate_num[:-1]):
        if c.isdigit():
            digits_found += 1
            numbers.append(int(c))

            if plate_num[i + 1].isalpha():
                return False

    if numbers[0] == 0 and digits_found > 0:
        return False
    else:
        return True

main()