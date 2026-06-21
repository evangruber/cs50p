def main():
    groceries = {}

    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            print()
            break

        if not item:
            continue

        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1

    for item in sorted(groceries):
        print(groceries[item], item)


main()
