class Vehicle:
    def __init__(self, n, ln):
        self._name = n
        self._last = ln

    def get_name(self):
        return self._first + " " + self._last


class Car(Vehicle):
    def __init__(self, fn, ln, gpa):
        super().__init__(fn, ln)  # or Person.__init__(fn, ln)
        self.gpa = gpa


class Truck(Vehicle):
    def __init__(self, fn, ln, num_stu):
        super().__init__(fn, ln)
        self.num_stu = num_stu


class Bus(Vehicle):
    def __init__(self, fn, ln, fav_word):
        super().__init__(fn, ln)
        self.fav_word = fav_word
