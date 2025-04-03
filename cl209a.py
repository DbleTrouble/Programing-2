class Counting:
    def __init__(self, nums):
        self.nums = nums
        self.total = 0.0
        self.greater = 0.0
        self.less = 0.0

    def calc(self):
        for num in self.nums
        if num < 500:
            self.less += 1
            self.total += 1
        elif self.num >= 500:
            self.greater += 1
            self.total += 1
        else:
            print("Error")



    def __str__(self):
        return f"The number of numbers less than 500 is {self.less}"
        return f"The number of numbers greater than or equal to 500 is {self.greater}"
        return f"The total number of numbers is {self.total}"
