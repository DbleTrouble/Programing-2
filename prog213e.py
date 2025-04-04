class Family:
    def __init__(self, num):
        self.e = None
        self.d = None
        self.c = None
        self.b = None
        self.a = None
        self.num = num
        self.age1 = []
        self.age2 = []
        self.age3 = []
        self.age4 = []
        self.age5 = []
        self._budget = 0
        self._percents = [0]*4  # [0,0,0,0]

    def sort(self):
        if self.num < 20:
            self.age1.append(self.num)
        elif 20 <= self.num <= 39:
            self.age2.append(self.num)
        elif 40 <= self.num <= 59:
            self.age3.append(self.num)
        elif 60 <= self.num <= 79:
            self.age4.append(self.num)
        elif self.num > 79:
            self.age5.append(self.num)

    # def _get_percent(self, number):
    #     return round((number/self._budget) * 100, 2)

    def calculate(self):
        # self._budget = self.age1 + self.age2 + self.age3 + self.age4 + self.age5
        # self._percents[0] = self._get_percent(len(self.age1))
        # self._percents[1] = self._get_percent(len(self.age2))
        # self._percents[2] = self._get_percent(len(self.age3))
        # self._percents[3] = self._get_percent(len(self.age4))
        # self._percents[4] = self._get_percent(len(self.age5))
        self.a = ((len(self.age1)/len(self.num)) * 100, 2)
        self.b = ((len(self.age2)/len(self.num)) * 100, 2)
        self.c = ((len(self.age3)/len(self.num)) * 100, 2)
        self.d = ((len(self.age4)/len(self.num)) * 100, 2)
        self.e = ((len(self.age5)/len(self.num)) * 100, 2)

    def display(self):
        print("Task\t\t% Time")
        print(f"Ages < 20:\t{self.age1}\t{self.a}%")
        print(f"Ages 20 - 39:\t{self.age2}\t\t{self.b}%")
        print(f"Ages 40 - 59:\t{self.age3}\t{self.c}%")
        print(f"Ages 60 - 79:\t{self.age4}\t{self.d}%")
        print(f"Ages > 79:\t{self.age5}\t{self.e}%")


def main():
    num = []
    with open("langdat/prog213e.dat", 'r') as f:
        for line in f:
            num.append(int(line))


    # Make a new 'Budget' object, pass in the numbers to the constructor
    spending = Family(num)
    spending.sort()
    spending.calculate()
    spending.display()
    pass

if __name__ == "__main__":
    main()

