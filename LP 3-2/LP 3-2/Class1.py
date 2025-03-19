
class Class1:
    def __init__(self, diameter):
        self.diameter = diameter
        self.cost = 0
        
    def calculate_cost(self):
        self.cost = (0.05 * self.diameter * self.diameter) + 0.75 + 1.00
        pass
