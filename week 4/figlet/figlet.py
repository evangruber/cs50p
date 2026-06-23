import sys
from pyfiglet import Figlet, FontNotFound
from random import choice


def main():

    figlet = Figlet()
    #Error Checking: if 0 or 2 arguments passed to command line
    if len(sys.argv) == 1 or len(sys.argv) == 3:

        #Error Checking: if first argument is -f or --font (user specified a font)
        if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):

            try:
                figlet.setFont(font = sys.argv[2])
            except FontNotFound:
                sys.exit("Invalid usage")

            text = input("Input: ")

        #if user did not specify a font
        elif len(sys.argv) == 1:

            text = input("Input: ")

            figlet.setFont(font = choice(figlet.getFonts()))

        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
