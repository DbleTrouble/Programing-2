class Family:
    def __init__(self, age):
        self.age = age
        self.percent = 0.0
        self.D = [D1, D2, D3, D4, D5]
        D1 = 0
        D2 = 0

    def calc(self):
        if self.age < 20:
            D1 += 1
        elif 20 <= self.age <= 39:
            D2 += 1
        elif 40 <= self.age >= 59:
            D3 += 1
        elif 60 <= self.age >= 79:
            D4 += 1
        elif self.age > 79:
            D5 += 1

    def __str__(self):
        print(f"The Distribution of {self.age} is ${D1:.2f}")
        print(f"The Distribution of {self.age} is ${D2:.2f}")
        print(f"The Distribution of {self.age} is ${D3:.2f}")
        print(f"The Distribution of {self.age} is ${D4:.2f}")
        print(f"The Distribution of {self.age} is ${D5:.2f}")
