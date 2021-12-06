import csv

def main():
    cnt = 0

    try:
        with open("./input") as f:
            reader = csv.reader(f)
            char_map = []
            gamma = epsilon = ""
            for line in reader:
                line_char_map = []
                for char in line[0]:
                    line_char_map.append(char)
                char_map.append(line_char_map)

            for i in range(len(char_map[0])):
                zero = one = 0;
                for line in char_map:
                    if line[i] == "0":
                        zero += 1
                    else:
                        one += 1
                gamma += "0" if zero >= one else "1"
                epsilon += "1" if zero >= one else "0"
            print(int(gamma, 2) * int(epsilon, 2))


    finally:
        f.close()


if __name__ == "__main__":
    main()