import csv

def main():
    cnt = 0

    try:
        with open("./input") as f:
            reader = csv.reader(f)
            map = draw_map(reader)
            count = 0
            for key, val in map.items():
                if val >= 2:
                    count += 1
            print(count)
    finally:
        f.close()

def draw_map(reader):
    map = {}
    for line in reader:
        coords = parse_line(line)
        is_reverse = False if coords[0] <= coords[2] else True
        if is_horz_or_vert(coords):
            if is_horz(coords):
                fill_line(map, coords[0], coords[2], coords[1], 1 if coords[0] <= coords[2] else -1, 0)
            else:
                fill_line(map, coords[1], coords[3], coords[0], 1 if coords[1] <= coords[3] else -1, 1)
        else:
            a = coords[2] if is_reverse else coords[0]
            b = coords[0] if is_reverse else coords[2]
            c = coords[3] if is_reverse else coords[1]
            d = coords[1] if is_reverse else coords[3]
            fill_diag_line(map, a, b, c, d)
    return map

def fill_diag_line(map, a, b, c, d):
    b += 1
    d += 1 # 0,0 -> 3,3
    for i in range(a, b):
        key = str(i) + "," + str(c)
        if key in map:
            map[key] += 1
        else:
            map[key] = 1
        if d > c:
            c += 1
        else:
            c -= 1

def fill_line(map, a, b, c, dir, axis):
    if dir == 1:
        b += 1
    else:
        b -= 1
    for i in range(a, b, dir):
        key = str(i) + "," + str(c) if axis == 0 else str(c) + "," + str(i)
        if key in map:
            map[key] += 1
        else:
            map[key] = 1

def is_horz_or_vert(coords):
    return (coords[0] == coords[2]) or (coords[1] == coords[3])

def is_horz(coords):
    return coords[1] == coords[3]

def parse_line(line):
    middle = line[1].split(" -> ")
    new_line = [int(line[0]), int(middle[0]), int(middle[1]), int(line[2])]
    return new_line

if __name__ == "__main__":
    main()