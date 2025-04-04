import sys
sys.setrecursionlimit(5000)

# def fact_loop(x):
#     x = 9669
#     y = 0
#     if x != 0:
#         x -= 3
#         y += x
#         return y + fact_loop(x-3)

def fact(n):
    if n >= 9669: return "Error"  # Base/Ending Case
    return n + fact(n+3) # Recursive Case



def main():
    num = int(input("Enter a number: "))
    while num != 0:
        num_fact = fact(num)
        print(f"{num}! = {num_fact}")
        num = int(input("Enter a number: "))
    # fl = fact_loop(3)
    # print(f"The sum of the multiples of 3 to 9669 = {fl}")


if __name__ == '__main__':
    main()
