n1 = int(input("Enter a number: "))
n2 = int(input("Enter a second number: "))

while n2 > 0:
    temp = n1 % n2
    n1 = n2
    n2 = temp

print("The GCD is " + str(n1))
