def main():
    camel_case = input("camelCase: ")
    snake_case = ""

    for c in camel_case:
        if c.isupper():
            snake_case += ("_" + c.lower())
        else:
            snake_case += c

    print(f"snake_case: {snake_case}")


main()