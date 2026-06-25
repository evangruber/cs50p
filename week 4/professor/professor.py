import random


def main():

    level = get_level()

    question = score = 0

    while question < 10:

        error = 0
        question += 1

        x = generate_integer(level)
        y = generate_integer(level)

        while error < 3:

            print(f"{x} + {y} = ", end="")

            try:
                answer = int(input(""))
            except ValueError:
                error += 1
                print("EEE")
                continue

            if answer == (x + y):
                score += 1
                break
            else:
                error += 1
                print("EEE")

            if error == 3:
                print(f"{x} + {y} = {x + y}")
                break

    print(f"Score: {score}")


def get_level():
    level = 0

    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass

        if level in [1, 2, 3]:
            return level


def generate_integer(level):

    if level == 1:
        low, high = 0, 9
    elif level == 2:
        low, high = 10, 99
    else:
        low, high = 100, 999

    return random.randint(low, high)


if __name__ == "__main__":
    main()
