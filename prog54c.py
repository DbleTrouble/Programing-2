import VoidFunctions

def calcArea(radius) -> int:
    return 3.14159 * radius

def calcCircu(radius) -> int:
    return 2*3.14159*radius

def areaPerim(radius):
    area = calcArea(radius)
    circumference = calcCircu(radius)
    return area, circumference

def main():
    VoidFunctions.doThing()
    radius = int(input("Enter Radius: "))
    a, c = areaPerim(radius)
    print(f"Area: {a}\nCircumference: {c}")
    pass

if __name__ == "__main__":
    main()
