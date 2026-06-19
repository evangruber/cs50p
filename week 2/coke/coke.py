def main():
    amount_due = 50
    coin = 0

    while amount_due > 0:
        
        print(f"Amount Due: {amount_due}")
        
        coin = int(input("Insert Coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            amount_due -= coin
        
        coin = 0
        
    print(f"Change Owed: {amount_due * -1}")


main()