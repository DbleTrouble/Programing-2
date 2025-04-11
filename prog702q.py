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
                    mw = float(f.readline())
                    v = Car(na, tr, va, mw)
                    vehicle.append(v)
                elif num == 2:
                    mpd = float(f.readline())
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
            large = ""
            small = "ljksdhfgkjdshgkjdjkhgkjsdkjdvbkjsbviuewbuidsbjkbzlliubwubi"
            for person in vehicle:
                if isinstance(vehicle, Car):
                    tot += vehicle.mw
                    cnt += 1
                elif isinstance(vehicle, Truck):
                    tot_stus += vehicle.mpd
                elif isinstance(vehicle, Bus):
                    fw = vehicle.hc
                    if len(fw) > len(large):
                        large = fw
                    if len(fw) < len(small):
                        small = fw
            print("Average student GPA:", round(tot/cnt, 2))
            print("Total number of students taught:", tot_stus)
            print("Smallest favorite admin word:", small)
            print("Largest favorite admin word:", large)
    except OSError as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
