#!/usr/bin/python

# 987654321111111
def find_voltage(bank):
    bank = bank.strip()
    first = bank[0]
    num = 0
    for i in range(0, len(bank)):
      first = bank[i]
      for x in range(0, len(bank)):
          if x > i:
            second = bank[x]
            if int(first + second) > num:
              num = int(first + second)
    return num

def find_big_voltage(bank):
    bank = bank.strip()
    numbers = [int(e) for e in str(bank)]
    battery_map = []
    for n in numbers:
        battery_map.append([n, 0])

    last_index = 0
    while (True):
        lit = len(list(filter(lambda x: x[1] == 1, battery_map)))
        if lit < 12:
            highest = [0, 0]
            # find highest and switch on
            for i, x in enumerate(battery_map):
                if i < last_index:
                    continue
                if x[1] == 0 and x[0] > highest[0] and i <= len(battery_map) - (12 - lit):
                    highest = x
                    last_index = i
            highest[1] = 1
            if last_index >= len(battery_map) - 11:
                for i in range(last_index, len(battery_map)):
                    battery_map[i][1] == 1
                lit = len(list(filter(lambda x: x[1] == 1, battery_map)))
                if lit == 12:
                    break
        else:
            break
    batteries = list(filter(lambda x: x[1] == 1, battery_map))
    batteries = list(map(lambda x: str(x[0]), batteries))
    return batteries

f = open('3.txt')
voltage = 0
for r in f:
    voltage += int("".join(find_big_voltage(r)))
print(voltage)

