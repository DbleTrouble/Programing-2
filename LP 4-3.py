eggs = int(input("Enter the total number of eggs: "))
dozens = eggs // 12
remainder = eggs % 12
price = 0.0
cost = 0.0

if 0 <= dozens < 4:
    price = 0.50
elif 4 <= dozens < 6:
    price = 0.45
elif 6 <= dozens < 11:
    price = 0.40
elif dozens >= 11:
    price = 0.35
else:
    print("Invalid number of eggs!")



cost = dozens * price + (remainder * 1.0/12 * price)
print("Price per eggs is $" + str(price))
print("Total cost is $" + str(round(cost,2)))