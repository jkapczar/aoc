p = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5,"BZ": 9, "CX":2,"CY":6,"CZ":7}
points = 0
with open("input.txt", "r") as f:
  for line in f.readlines():
    s = line[0] + line[2]
    print(s, p[s])
    points += p[s]

print(points)
