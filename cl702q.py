class Vehicle:
    def __init__(self, na, tr, ):
        self._name = na
        self._tire = tr


    def get_vehicles(self):
        return self._name + self._tire


class Car(Vehicle):
    def __init__(self, na, tr, va):
        super().__init__(na, tr)  # or Person.__init__(fn, ln)
        self.va = va
        print(na)
        print(tr)
        print(va)


class Truck(Vehicle):
    def __init__(self, na, tr, va, mpd):
        super().__init__(na, tr)
        self.va = va
        self.mpd = mpd
        va = 50000 - (mpd * .25)
        print(na)
        print(tr)
        print(va)


class Bus(Vehicle):
    def __init__(self, na, tr, hc):
        super().__init__(na, tr)
        self.hc = hc
        print(na)
        print(tr)
        print(hc)

