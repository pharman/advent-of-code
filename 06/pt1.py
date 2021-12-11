import csv

def main():
    cnt = 0

    try:
        with open("./input") as f:
            reader = csv.reader(f)
            shoal = list(map(int, next(reader)))

            for _ in range(0, 80):
                for index, fish in enumerate(shoal):
                    if fish == 0:
                        shoal[index] = 6
                        shoal.append(9)

                    else:
                        shoal[index] -= 1
            print(len(shoal))

    finally:
        f.close()

if __name__ == "__main__":
    main()