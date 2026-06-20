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

    if not (2 <= len(s) <= 6):
        return False

    if not s[:2].isalpha() or not s.isalnum():
        return False

    digit_started = False

    for c in s[2:]:
            # Find the first digit
        if c.isdigit():
            if not digit_started:
                digit_started = True

                # Check if the first digit is 0
                if c == "0":
                    return False

        # Check if letters are included after the first digit
        elif digit_started:
            return False

    return True


main()
