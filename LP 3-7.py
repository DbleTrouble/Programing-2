def calculate(x,y):
        a = x / y
        b = x % y

        c = y / x
        d = y % x
        
        return(a, b, c, d)


def main():
    

    Int1 = float(input("Integer 1: "))
    Int2 = float(input("Integer 2: "))
    f = calculate(Int1,Int2)
    print(f)
    

    pass


if __name__ == "__main__":
    main()
