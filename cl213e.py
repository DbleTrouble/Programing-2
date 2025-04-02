class Family:
    def __init__(self, ages):
        self.ages = ages
        self.distribution = 0.0
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.d = 0.0
        self.e = 0.0
        self.percent = 0.0

    def calc(self):
        for age in self.ages:
            if age < 20:
                self.distribution += 1
                self.a += 1
            elif 20 <= age <= 39:
                self.distribution += 1
                self.b += 1
            elif 40 <= age <= 59:
                self.distribution += 1
                self.c += 1
            elif 60 <= age <= 79:
                self.distribution += 1
                self.d += 1
            elif age > 79:
                self.distribution += 1
                self.e += 1
        # TODO calcute percent
        self.percent = ( self.a / self.distribution) * 100
        self.percent = ( self.b / self.distribution) * 100
        self.percent = ( self.c / self.distribution) * 100
        self.percent = ( self.d / self.distribution) * 100
        self.percent = ( self.e / self.distribution) * 100
    def get_distribution(self):
        return self.distribution

    def __str__(self):
        print(f"The percent of distribution {self.a} is {self.percent:.2f}%")
        print(f"The percent of distribution {self.b} is {self.percent:.2f}%")
        print(f"The percent of distribution {self.c} is {self.percent:.2f}%")
        print(f"The percent of distribution {self.d} is {self.percent:.2f}%")
        print(f"The percent of distribution {self.e} is {self.percent:.2f}%")
