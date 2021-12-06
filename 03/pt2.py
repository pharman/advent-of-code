import csv

def main():
    cnt = 0

    try:
        with open("./input") as f:
            reader = csv.reader(f)
            char_map = []
            for line in reader:
                line_char_map = []
                for char in line[0]:
                    line_char_map.append(char)
                char_map.append(line_char_map)
            oxygen_rating = recurse(char_map, 0, lambda zeros, ones: len(zeros) > len(ones))
            co2_rating = recurse(char_map, 0, lambda zeros, ones: len(ones) >= len(zeros))
            print(int("".join(oxygen_rating[0]), 2) * int("".join(co2_rating[0]), 2))


    finally:
        f.close()

def recurse(char_map, depth, comparison):
    if len(char_map) == 1:
        return char_map
    ones = []
    zeros = []
    for line in char_map:
        if line[depth] == "0":
            zeros.append(line)
        else:
            ones.append(line)
    return recurse(zeros, depth +1, comparison) if comparison(zeros, ones) else recurse(ones, depth +1, comparison)

if __name__ == "__main__":
    main()