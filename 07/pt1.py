import csv

def main():

    try:
        with open("./input") as f:
            reader = csv.reader(f)
            crabs = list(map(int, next(reader)))
            costs = []
            for crab in crabs:
                cost = 0
                for match_crab in crabs:
                    cost += match_crab - crab if match_crab > crab else crab - match_crab
                costs.append(cost)
            costs.sort()
            print(costs[0])


    finally:
        f.close()

if __name__ == "__main__":
    main()