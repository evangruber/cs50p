def main():

    text = input("Input: ")

    print(f"{shorten(text)}")


def shorten(word):

    for letter in word:
        if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            word = word.replace(letter, "")

    return word

if __name__ == "__main__":
    main()
