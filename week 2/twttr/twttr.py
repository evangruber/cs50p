def main():
    tweet = input("Input: ")

    print(f"Output: {shorten_tweet(tweet)}")


def shorten_tweet(text):
    vowels = ("a", "e", "i", "o", "u")

    for c in text:
        for vowel in vowels or vowels.upper():
            if c.lower() == vowel:
                text = text.replace(c, "")

    return text


main()
