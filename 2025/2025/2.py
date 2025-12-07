#!/usr/bin/python

import csv

def find_invalid(d):
  d = d.split("-")
  m = []
  for x in range(int(d[0]), int(d[1]) +1):
    c = [int(e) for e in str(x)]
    left = c[:len(c)//2]
    right = c[len(c)//2:]
    if left == right:
      m.append(x)
  return m

def find_any_invalid(d):
  d = d.split("-")
  m = set()
  for x in range(int(d[0]), int(d[1]) +1):
    c = [int(e) for e in str(x)]

    for n in range(1, len(c)):
      chunks = [c[i:i + n] for i in range(0, len(c), n)]
      if (all(map(lambda x: x == chunks[0], chunks))):
        m.add(x)
  return m

    
f = open('2.txt')
c = csv.reader(f)
i = []
for r in c:
  for d in r:
    i = i + list(find_any_invalid(d))
z = 0
for n in i:
  z += n

print(z)
 


