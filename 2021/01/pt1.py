import csv

def main():
    cnt = 0

    try:
        with open("input") as f:
            reader = csv.reader(f)
            prev = None;
            count = 0;
            for line in reader:
                num = int(line[0])
                if prev != None and num > prev:
                    count += 1
                prev = num

        print(count)

    finally:
        f.close()


if __name__ == "__main__":
    main()