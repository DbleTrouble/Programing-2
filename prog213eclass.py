from cl213e import Family

def main():
    try:
        with open("langdat/prog213e.dat", 'r') as f:
        or line in f:
                kwh = int(line)
                if kwh != -999:
                    e_bill = ElectricBill(kwh)
                    bills.append(e_bill)
        for bill in bills:
            bill.calc()
            print(bill) # print(str(bill))
    except OSError as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
