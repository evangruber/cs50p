from random import randint


def main():
    level = get_level()

    answer = randint(1, level)

    guess = 0

    while guess != answer:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        if guess <= 0:
            continue
        elif guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        else:
            print("Just right!")


def get_level():
    level = 0

    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level <= 0:
            continue
        else:
            break

    return level

if __name__ == "__main__":
    main()
