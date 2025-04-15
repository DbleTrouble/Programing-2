from cl702q import *


def main():
    try:
        vehicle: list[Vehicle] = []
        with open("langdat/prog701g.dat", 'r') as f:
            num = int(f.readline())
            while num != 99:
                na = f.readline()
                tr = f.readline()
                va = f.readline()
                if num == 1:
                    v = Car(na, tr, va,)
                    vehicle.append(v)
                elif num == 2:
                    mpd = int(f.readline().strip())
                    v = Truck(na, tr, va, mpd)
                    vehicle.append(v)
                elif num == 3:
                    hc = f.readline().strip()
                    v = Bus(na, tr, va, hc)
                    vehicle.append(v)
                num = int(f.readline())
            tot = 0.0
            cnt = 0
            tot_stus = 0

            for vehicle in vehicle:
                if isinstance(vehicle, Car):
                    tot += vehicle.mw
                    cnt += 1
                elif isinstance(vehicle, Truck):
                    tot_stus += vehicle.mpd
                elif isinstance(vehicle, Bus):
                    fw = vehicle.hc


    except OSError as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
