import csv

def main():
    cnt = 0

    try:
        with open("input") as f:
            reader = csv.reader(f)
            horz = 0
            depth = 0
            for line in reader:
                command = line[0].split(" ")
                num = int(command[1])
                if command[0] == "forward":
                    horz += num
                if command[0] == "down":
                    depth += num
                if command[0] == "up":
                    depth -= num
            print(horz * depth)

    finally:
        f.close()


if __name__ == "__main__":
    main()