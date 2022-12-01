import csv

def main():
    cnt = 0

    try:
        with open("input") as f:
            reader = csv.reader(f)
            horz = depth = aim = 0
            for line in reader:
                command = line[0].split(" ")
                num = int(command[1])
                if command[0] == "forward":
                    horz += num
                    depth += num * aim
                if command[0] == "down":
                    aim += num
                if command[0] == "up":
                    aim -= num
            print(horz * depth)

    finally:
        f.close()


if __name__ == "__main__":
    main()