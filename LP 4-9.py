import random
player = int(input("Enter a number between 1 and 20: "))

comp = random.randint(1,20)
print(str(comp))
print(str(player))

if player == comp:
    print("You won!")
else:
    print("Better luck next time.")
