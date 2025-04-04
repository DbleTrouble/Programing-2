class Counting:
    def __init__(self,nums):
        self.nums = nums
        self.greater = 0
        self.less = 0



    def calc(self):
        for x in self.nums:
            if x < 500:
                self.less += 1
            elif x >= 500:
                self.greater += 1
            else:
                print("Error")

    def display(self):
        print(f"The number of numbers less than 500 is {self.less}")
        print(f"The number of numbers greater than or equal to 500 is {self.greater}")
        print(f"The total number of numbers is {len(self.nums)}")

def main():
    nums = []
    with open("langdat/prog215a.dat", 'r') as f:
                    for line in f:
                        nums.append(int(line))

    c = Counting(nums)
    c.calc()
    c.display()


if __name__ == "__main__":
    main()
