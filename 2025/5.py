#!/usr/bin/python

def parse(row):
    ranges = []
    ingredients = []
    for line in lines:
        line = line.strip()
        if "-" in line:
            ranges.append(list(map(int, line.split("-"))))
        elif line == "":
            continue
        else:
            ingredients.append(int(line))
    return ranges, ingredients

def is_in_range(ingredient, ranges):
    for r in ranges:
        if ingredient >= r[0] and ingredient <= r[len(r)-1]:
            return 1
    return 0

def get_fresh_ids(ranges):
    ids = 0
    # Remove overlaps
    ranges = sorted(ranges, key=lambda x: x[0])
    merged = [ranges[0]]
    
    for current in ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1] + 1:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    
    for r in merged:
        ids += (r[1] - r[0]) + 1
    return ids

with open('5.txt') as file:
    lines = [line.rstrip() for line in file]
ranges, ingredients = parse(lines)
fresh = 0
for i in ingredients:
    fresh += is_in_range(i, ranges)
print(fresh)

print(get_fresh_ids(ranges))

