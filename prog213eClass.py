from cl213e import Family

def main():
    try:
        with open("langdat/prog213e.dat", 'r') as f:
            for line in f:
                age = int(line)
                if age != -999:
                    Dis = Family(age)
                    bills.append(Dis)
        for bill in bills:
            bill.calc()
            print(bill) # print(str(bill))
    except OSError as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
