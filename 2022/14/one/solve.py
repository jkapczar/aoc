def insertNewPozToDict(p, d):
  if p[0] not in d:
    d[p[0]] = [p[1]]
  else:
    tmp = d[p[0]] + [p[1]]
    d[p[0]] = list(set(tmp))
  return dict(sorted(d.items()))

def processCords(line, d):
  cords = [x.strip() for x in line.split("->")]
  cords = [[int(cords.split(",")[0]), int(cords.split(",")[1])] for cords in cords]
  return appendMissingCords(cords, d)

def appendMissingCords(cords, d):
  for i in range(len(cords)):
    if i+1 < len(cords):
      d = addMissing(cords[i], cords[i+1], d)
    else:
      d = insertNewPozToDict(cords[i], d)
  return d

def addMissing(currentC, nextC, d):
  if currentC[0] == nextC[0]:
    for i in range(min(currentC[1], nextC[1]), max(currentC[1], nextC[1])):
      d = insertNewPozToDict([currentC[0], i], d)
  if currentC[1] == nextC[1]:
    for i in range(min(currentC[0], nextC[0]), max(currentC[0], nextC[0])):   
      d = insertNewPozToDict([i, currentC[1]], d)
  return insertNewPozToDict(currentC, d)

def calcNextPossiblePoz(p, d, m):
  while True:
    #print(f"p: {p}")
    if p[1] > m: return p, True
    if p[0] not in d or p[1] + 1 not in d[p[0]]:
      p = [p[0], p[1] + 1]
    else:
      if p[1] + 1 > m: return p, True
      if p[0] - 1 not in d or p[1] + 1 not in d[p[0] - 1]:
        p = [p[0] - 1, p[1] + 1]
      else:
        if p[1] + 1 > m: return p, True
        if p[0] + 1 not in d or p[1] + 1 not in d[p[0] + 1]:
          p = [p[0] + 1, p[1] + 1]
        else:
          return p, False

def fall(d, m):
  c = -1
  stop = False
  start = [500, 0]
  while not stop:
    c += 1
    p, stop = calcNextPossiblePoz(start, d, m)
    d = insertNewPozToDict(p, d)
    print(f"point p: {p} added and c now is: {c}")
    print("------------------------")
    print()
  print(c)

d = {}
with open("input.txt", "r")  as f:
  for line in f.readlines():
    d = processCords(line.strip(), d)

m = 0
for v in d.values():
  cmax = max(v)
  if cmax > m: m = cmax

print(d, m)
fall(d, m)
