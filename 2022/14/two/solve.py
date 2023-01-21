def processCords(line):
  cords = [x.strip() for x in line.split("->")]
  cords = [[int(cords.split(",")[0]), int(cords.split(",")[1])] for cords in cords]
  return appendMissingCords(cords)

def appendMissingCords(cords):
  tmp = []
  for i in range(len(cords)):
    if i+1 < len(cords):
      addMissingPozitions(tmp, cords[i], cords[i+1])
    else:
      tmp.append(cords[i])
  return tmp

def addMissingPozitions(tmp, currentC, nextC):
  if currentC[0] == nextC[0]:
    for i in range(min(currentC[1], nextC[1]), max(currentC[1], nextC[1])):
      tmp.append([currentC[0], i])
  if currentC[1] == nextC[1]:
    for i in range(min(currentC[0], nextC[0]), max(currentC[0], nextC[0])):
      tmp.append([i, currentC[1]])
  tmp.append(currentC)

def transform(r):
  d = {}
  m = 0
  for i in r:
    for j in i:
      if j[0] in d:
        tmp =  d[j[0]] + [j[1]]
        d[j[0]] = sorted(set(tmp))
      else:
        d[j[0]] = [j[1]]
      cmax = max(d[j[0]])
      if cmax > m:
        m = cmax
  for i in range(0, 1000):
    if i in d:
      tmp = d[i] + [m + 2]
      d[i] = sorted(set(tmp))
    else: 
      d[i] = [m + 2]
  return m, dict(sorted(d.items()))

def calcNextPossiblePoz(p, d, m):
  while True:
    #print(f"p: {p}")
    if p[1] > m: return p
    if p[0] not in d or p[1] + 1 not in d[p[0]]:
      p = [p[0], p[1] + 1]
    else:
      if p[1] + 1 > m: return p
      if p[0] - 1 not in d or p[1] + 1 not in d[p[0] - 1]:
        p = [p[0] - 1, p[1] + 1]
      else:
        if p[1] + 1 > m: return p
        if p[0] + 1 not in d or p[1] + 1 not in d[p[0] + 1]:
          p = [p[0] + 1, p[1] + 1]
        else:
          return p

def insertNewPozToDict(p, d):
  print(p)
  if p[0] not in d:
    d[p[0]] = [p[1]]
  else:
    tmp = d[p[0]] + [p[1]]
    d[p[0]] =  sorted(set(tmp))
  return dict(sorted(d.items()))

def fall(d, m):
  c = 0
  start = [500, 0]
  while True:
    c += 1
    p = calcNextPossiblePoz(start, d, m)
    d = insertNewPozToDict(p, d)
    if p[0] == 500 and p[1] == 0: break
    print(f"point p: {p} added and c now is: {c}")
    print("------------------------")
    print()
  print(c)

r = []
with open("input.txt", "r")  as f:
  for line in f.readlines():
    r.append(processCords(line.strip()))

m, d = transform(r)
m += 2
print(d)
fall(d, m)



