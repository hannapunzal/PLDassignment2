enter_Money = int(input("Enter the amount of money you have: "))
apple_Price = int(input("Enter the price of the apple: "))

apple_Total = int(enter_Money/apple_Price)
cost_Total = apple_Total * apple_Price
money_Change = enter_Money - cost_Total
print(f"You can buy {apple_Total} apples and your change is PHP{money_Change}.")