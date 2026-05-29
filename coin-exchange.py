#coin exchange
def change(amount):
    coins = [2000, 500, 200, 100, 50, 20 ,10, 5, 2, 1]
    print("Coins used: ")
    for c in coins:
        if amount >= c:
            count = amount//c
            amount = amount%c
            print(c, "X", count)
amount = int(input("Enter the amount: "))
change(amount)