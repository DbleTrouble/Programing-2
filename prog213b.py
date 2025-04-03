class Ordering:
    def __init__(self,quantity):
        self.quantity = quantity
        self.price = 0.0
        self.cost = 0.0

    def calc(self):
        if self.quantity <= 99:
            self.price = 5.95
            self.cost = self.quantity * self.price
        elif 99 < self.quantity <= 199:
            self.price = 5.75
            self.cost = self.quantity * self.price
        elif 199 < self.quantity <= 299:
            self.price = 5.40
            self.cost = self.quantity * self.price
        elif 299 < self.quantity:
            self.price = 5.15
            self.cost = self.quantity * self.price

    def display(self):
        print(f"Price: ${self.price}")
        print(f"Cost: ${self.cost}")

def main():
    quantity = float(input("Enter quantity: "))
    x = Ordering(quantity)
    x.calc()
    x.display()


if __name__ == "__main__":
    main()
