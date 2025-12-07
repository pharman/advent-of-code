#!/usr/bin/python

import math

pos = 50
password = 0

def two(input, clicks):
  global pos, password
  num = parse(input)

  pos += num

  print("pos"+str(pos))

  pos_num = pos
  if pos_num < 0:
    pos_num = pos_num - (pos_num * 2)
    if pos_num < 100:
      pos_num += 100
  if pos_num > 100:
    click = math.floor(pos_num / 100)
    print("click" + str(click))
    password += click
  if pos == 0:
    password += 1

def parse(input):
  input = input.strip()
  dir = input[0:1]
  num = int(input[1:])
  if dir == "L":
      num = num - (num * 2)
  return num


#f = open('1.txt')
#for input in f:
#  two(input, False)
#print(password)

pos = 50
password = 0
f = open('1.txt')
for input in f:
  two(input, True)
print(password)


