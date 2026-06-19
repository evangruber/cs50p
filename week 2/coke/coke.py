def main():
    amount_due = 50
    coin = 0

    print(f"Amount Due: {amount_due}")

    while amount_due > 0:
        while True:
            coin = int(input("Insert Coin: "))

            if coin != 25 and coin != 10 and coin != 5:
                print(f"Amount Due: {amount_due}")
            else:
                break

        amount_due -= coin

        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        else:
            print(f"Change Owed: {amount_due * -1}")
            break

        coin = 0

main()