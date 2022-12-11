p = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5,"BZ": 9, "CX":7,"CY":2,"CZ":6}
points = 0
with open("input.txt", "r") as f:
  for line in f.readlines():
    s = line[0] + line[2]
    print(s, p[s])
    points += p[s]

print(points)
