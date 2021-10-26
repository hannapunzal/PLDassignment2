apple_Question = int(input("How many apples do you want to buy?"))
orange_Question = int(input("How many oranges do you want to buy?"))

apple_Price = 20
orange_Price = 35

apple_Total = apple_Question * apple_Price
orange_Total = orange_Question * orange_Price
total = apple_Total + orange_Total
print(f"The total amount for the apples and oranges is PHP{total}.")