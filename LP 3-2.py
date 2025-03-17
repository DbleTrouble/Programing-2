def calculate(x):
        a = (0.05 * x * x) + 0.75 + 1.00
        
        return(a)


def main():
    

    D = float(input("Enter the diameter of the pizza in inches: "))
    f = calculate(D)
    print(f)
    

    pass


if __name__ == "__main__":
    main()