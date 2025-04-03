from cl209a import Counting

def main():
    try:
        nums = []
        with open("langdat/prog215a.dat", 'r') as f:
            for line in f:
                num = int(line)
                if num != -999:
                    nums.append(num)

        thing = Counting(nums)
        thing.calc()
        print(thing)
    except OSError as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
