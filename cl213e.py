class Family:
    def __init__(self, age1, age2, age3, age4, age5):
        self.age = age
        self._distribution = 0
        self._percents = [0]*4

    def _get_percent(self, number):
        return round((number/self._distribution) * 100, 2)

    def calculate(self):
        self._budget = self.age1 + self.age2 + self.age3 + self.age4 + self.age5
        self._percents[0] = self._get_percent(self.age1)
        self._percents[1] = self._get_percent(self.age2)
        self._percents[2] = self._get_percent(self.age3)
        self._percents[3] = self._get_percent(self.age4)
        self._percents[4] = self._get_percent(self.age5)

    def display(self):
        print("Task\t\t% Time")
        print(f"age1:\t{self._percents[0]}%")
        print(f"age2:\t\t{self._percents[1]}%")
        print(f"age3:\t{self._percents[2]}%")
        print(f"age4:\t{self._percents[3]}%")
        print(f"age5:\t{self._percents[4]}%")
