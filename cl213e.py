class Family:
    def __init__(self, ages):
        self.ages = ages
        self.distribution = 0.0
        self.percent = 0.0

    def calc(self):
        for age in self.ages:
            if age < 20:
                self.distribution += 1
            elif 20 <= age <= 39:
                self.distribution += 1
            elif 40 <= age <= 59:
                self.distribution += 1
            elif 60 <= age <= 79:
                self.distribution += 1

            elif age > 79:
                self.distribution += 1
        # TODO calcute percent
    def get_distribution(self):
        return self.distribution

    def __str__(self):
        return f"The percent of distribution {Family.get_distribution(self)} is {self.percent:.2f}%"
