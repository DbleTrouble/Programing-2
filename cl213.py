class ElectricBill:
    def __init__(self, kwh):
        self.kwh = kwh
        self.cost = 0.0

    def calc(self):
        if 0 < self.kwh <= 2000:
            self.cost += self.kwh * .07
        elif 2000 < self.kwh <= 10000:
            self.cost += self.kwh * .05
        elif self.kwh > 10000:
            self.cost += self.kwh * .04

    def __str__(self):
        return f"The cost of {self.kwh} is ${self.cost:.2f}"
