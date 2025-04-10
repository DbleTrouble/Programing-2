class Vehicle:
    def __init__(self, na, ml):
        self._name = na
        self._mile = ml

    def get_car(self):
        return self._name + " " + self._mile


class Car(Vehicle):
    def __init__(self, na, ml, mw):
        super().__init__(na, ml)  # or Person.__init__(fn, ln)
        self.mw = mw


class Truck(Vehicle):
    def __init__(self, na, ml, mpd):
        super().__init__(na, ml)
        self.mpd = mpd


class Bus(Vehicle):
    def __init__(self, na, ml, hc):
        super().__init__(na, ml)
        self.hc = hc
