class Vehicle:
    def __init__(self, na, tr, va):
        self._name = na
        self._tire = tr
        self._value = va

    def get_vehicles(self):
        return self._name + self._tire + self._value


class Car(Vehicle):
    def __init__(self, na, tr, va):
        super().__init__(na, tr, va)  # or Person.__init__(fn, ln)
        print(na)
        print(tr)
        print(va)


class Truck(Vehicle):
    def __init__(self, na, tr, va, mpd):
        super().__init__(na, tr, va)
        self.mpd = mpd
        va = 50000 - (mpd * .25)
        print(na)
        print(tr)
        print(va)


class Bus(Vehicle):
    def __init__(self, na, tr, va, hc):
        super().__init__(na, tr, va)
        self.hc = hc

