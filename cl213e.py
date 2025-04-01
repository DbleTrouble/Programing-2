class Family:
    def __init__(self, ages):
        self.ages = []
        self._budget = 0
        self._percents = [0]*5  # [0,0,0,0]

    def _get_percent(self, number):
        return round((number/self._budget) * 100, 2)

    def calculate(self):
        for self.age.append([1:5])
        self._budget = self.ages1 + self.ages2 + self.ages3 + self.ages4 + self.ages5
        self._percents[0] = self._get_percent(self.ages1)
        self._percents[1] = self._get_percent(self.ages2)
        self._percents[2] = self._get_percent(self.ages3)
        self._percents[3] = self._get_percent(self.ages4)
        self._percents[4] = self._get_percent(self.ages5)

    def display(self):
        print("Percentage")
        print(f"Age < 20:\t{self._percents[0]}%")
        print(f"Age 20 - 39:\t\t{self._percents[1]}%")
        print(f"Age 40 - 59:\t{self._percents[2]}%")
        print(f"Age 60 - 79:\t{self._percents[3]}%")
        print(f"Age > 79:\t{self._percents[4]}%")

def main():
    print("Enter the following distribution:\n")
    age1 = float(input("Age < 20: "))
    age2 = float(input("Age 20 - 39: "))
    age3 = float(input("Age 40 - 59: "))
    age4 = float(input("Age 60 - 79: "))
    age5 = float(input("Age > 79: "))
    print()

    # Make a new 'Budget' object, pass in the numbers to the constructor
    spending = Family(ages1, ages2, agse3, ages4, ages5)
    spending.calculate()
    spending.display()
    pass

if __name__ == "__main__":
    main()
