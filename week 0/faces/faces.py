def main():
    text = input()
    print(convert(text))

def convert(emoticon):
    emoji = emoticon.replace(":)", "🙂").replace(":(", "🙁")
    return emoji

main()
