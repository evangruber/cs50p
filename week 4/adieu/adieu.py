import inflect

def main ():
    p = inflect.engine()

    names = []

    while True:
        try:
            name = input("Name: ").strip().title()
        except EOFError:
            print()
            break

        names.append(name)

    print("Adieu, adieu, to " + p.join(names))



if __name__ == "__main__":
    main()
