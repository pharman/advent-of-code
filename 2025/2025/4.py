#!/usr/bin/python

def parse(row):
    data = []
    for r in row.strip():
        if r == ".":
            data.append(0)
        else:
            data.append(1)
    return data

# direction: -1 = left, 0 = centre, 1 = right
def is_adjacent(index, check_row, direction):
    if direction == -1 and index == 0:
        return False
    if direction == 1 and index >= len(check_row) -1:
        return False
    index = index + direction
    if check_row[index] == 1 or check_row[index] == 2:
        return True
    return False

def count_rolls(row, index, grid):
    accessible = 0
    for i in range(0, len(row)):
        if row[i] == 1:
            count = 0
            #left
            if is_adjacent(i, row, -1):
                count += 1
            #right
            if is_adjacent(i, row, 1):
                count += 1
            #row above
            if index > 0 and is_adjacent(i, grid[index-1], -1):
                count += 1
            if index > 0 and is_adjacent(i, grid[index-1], 0):
                count += 1
            if index > 0 and is_adjacent(i, grid[index-1], 1):
                count += 1
            # row below
            if index < len(grid) -1 and is_adjacent(i, grid[index+1], -1):
                count += 1
            if index < len(grid) -1 and is_adjacent(i, grid[index+1], 0):
                count += 1
            if index < len(grid) -1 and is_adjacent(i, grid[index+1], 1):
                count += 1
            if count < 4:
                row[i] = 2
                accessible += 1
    return accessible

def remove_cells(grid):
    for x in range(0, len(grid)):
        for i in range(0, len(grid[x])):
            if grid[x][i] == 2:
                grid[x][i] = 0


f = open('4.txt')
rolls = 0
prev_rolls = 0
grid = []
for r in f:
    grid.append(parse(r))

while True:
    prev_rolls = rolls
    for index, row in enumerate(grid):
        rolls +=  count_rolls(row, index, grid)
    remove_cells(grid)
    if prev_rolls == rolls:
        break

print(rolls)
