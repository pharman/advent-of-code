import csv

def main():
    cnt = 0

    try:
        with open("./input") as f:
            reader = csv.reader(f)
            shoal = list(map(int, next(reader)))
            shoal_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
            for fish in shoal:
                if fish in shoal_counts:
                    shoal_counts[fish] += 1
                else:
                    shoal_counts[fish] = 1
            print(shoal_counts)
            for _ in range(1, 257):
                new_fish = 0
                for i in range(0, 9):
                    num_fish_in_range = shoal_counts[i]
                    if i == 0:
                        new_fish = num_fish_in_range
                        shoal_counts[0] = 0
                    else:
                        shoal_counts[i-1] += num_fish_in_range
                        shoal_counts[i] = 0
                shoal_counts[8] += new_fish
                shoal_counts[6] += new_fish
            total = 0
            for fish in shoal_counts:
                total += shoal_counts[fish]
            print(total)

    finally:
        f.close()

if __name__ == "__main__":
    main()