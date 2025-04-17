from cl702q import *


def main():
    try:
        vehicle: list[Vehicle] = []
        with open("langdat/prog702q.txt", 'r') as f:
            num = int(f.readline().strip())
            while num != 99:
                na = f.readline().strip()
                tr = f.readline().strip()
                if num == 1:
                    va = float(f.readline().strip())
                    v = Car(na, tr, va,)
                    vehicle.append(v)
                elif num == 2:
                    mpd = int(f.readline().strip())
                    v = Truck(na, tr, va, mpd)
                    vehicle.append(v)
                elif num == 3:
                    hc = f.readline().strip()
                    v = Bus(na, tr, hc)
                    vehicle.append(v)
                num = int(f.readline())
    except OSError as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
