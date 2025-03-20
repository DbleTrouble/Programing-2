class Circle:
    # Constructor: sets up class data
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159
        self._area = 0   # _ prefix basically means 'private' so
        self._perim = 0  # it should only be called in the class

    # Mutator/Setter Method(s): modifies class data
    def calculate(self):
        self._area = self.pi * (self.radius**2)
        self._circum = 2 * self.pi * self.radius

    # Accessor/Getter Method(s): returns class data
    def get_area(self):
        return self._area

    def get_circumference(self):
        return self._circum


def main():
    radius = float(input("Enter radius: "))
    # Make a new 'Shape' object/instance
    circle = Circle(radius)  # Call 'Shape' constructor/__init__ method
    # shape.length = 5
    circle.calculate()
    print("Area: ", circle.get_area())
    print("Circumference: ", circle.get_circumference())
    pass


if __name__ == "__main__":
    main()
