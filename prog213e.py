from cl213e import Family

def main():
    try:
        ages = []
        with open("langdat/prog213e.dat", 'r') as f:
            for line in f:
                age = int(line)
                if ages != -999:
                    ages.append(age)
        thing = Family(ages)
        thing.calc()
        print(thing)
    except OSError as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
