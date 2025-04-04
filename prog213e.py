class Family:
    def __init__(self, age1, age2, age3, age4, age5):
            self.age1 = []
            self.age1 = age2
            self.age1 = age3
            self.age1 = age4
            self.age1 = age5
            self._budget = 0
            self._percents = [0]*4  # [0,0,0,0]

            with open("langdat/prog213e.dat", 'r') as f:
                        for line in f:
                            self.num.append(int(line))

        def _get_percent(self, number):
            return round((number/self._budget) * 100, 2)

        def calculate(self):
            self._budget = self.age1 + self.age2 + self.age3 + self.age4 + self.age5
            self._percents[0] = self._get_percent(self.self.age1)
            self._percents[1] = self._get_percent(self.self.age2)
            self._percents[2] = self._get_percent(self.self.age3)
            self._percents[3] = self._get_percent(self.self.age4)
            self._percents[4] = self._get_percent(self.self.age5)

        def display(self):
            print("Task\t\t% Time")
            print(f"designing:\t{self._percents[0]}%")
            print(f"coding:\t\t{self._percents[1]}%")
            print(f"debugging:\t{self._percents[2]}%")
            print(f"testing:\t{self._percents[3]}%")
            print(f"testing:\t{self._percents[4]}%")

def main():
    print("Enter the following items:\n")
    designing = float(input("Designing: "))
    coding = float(input("Coding: "))
    debugging = float(input("Debugging: "))
    testing = float(input("Testing: "))
    print()

    # Make a new 'Budget' object, pass in the numbers to the constructor
    spending = Budget(age1, age1, age1, age1, age5)
    spending.calculate()
    spending.display()
    pass

if __name__ == "__main__":
    main()

