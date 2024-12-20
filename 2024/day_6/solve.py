import sys

res = set()
m = []
p = (0, 0)
direction = "UP"

with open(sys.argv[1], "r") as f:
  for index, line in enumerate(f.readlines()):
    row = list(line.strip())
    if "^" in row:
      p = (index, row.index("^"))
      print(p)
    m.append(row)

def print_map():
  global m, p, direction, res
  print("MAP: ")
  for i in m:
    print(i)
  print(f"POZ: {p}, DIRECTION: {direction}")

def do_step():
  global m, p, direction
  if direction == "UP" and p[0] - 1 < 0: return False
  if direction == "UP" and m[p[0] - 1][p[1]] == "#":
    direction = "RIGHT"
    m[p[0]][p[1]] = ">"
    return do_step()
  if direction == "UP" and m[p[0] - 1][p[1]] == ".":
    m[p[0]][p[1]] = "."
    p = (p[0] - 1, p[1])
    m[p[0]][p[1]] = "^"
    return True

  if direction == "RIGHT" and p[1] + 1 == len(m[0]): return False
  if direction == "RIGHT" and m[p[0]][p[1] + 1] == "#":
    direction = "DOWN"
    m[p[0]][p[1]] = "v"
    return do_step()
  if direction == "RIGHT" and m[p[0]][p[1] + 1] == ".":
    m[p[0]][p[1]] = "."
    p = (p[0], p[1] + 1)
    m[p[0]][p[1]] = ">"
    return True

  if direction == "DOWN" and p[0] + 1 == len(m): return False
  if direction == "DOWN" and m[p[0] + 1][p[1]] == "#":
    direction = "LEFT"
    m[p[0]][p[1]] = "<"
    return do_step()
  if direction == "DOWN" and m[p[0] + 1][p[1]] == ".":
    m[p[0]][p[1]] = "."
    p = (p[0] + 1, p[1])
    m[p[0]][p[1]] = "v"
    return True

  if direction == "LEFT" and p[1] - 1 < 0: return False
  if direction == "LEFT" and m[p[0]][p[1] - 1] == "#":
    direction = "UP"
    m[p[0]][p[1]] = "^"
    return do_step()
  if direction == "LEFT" and m[p[0]][p[1] - 1] == ".":
    m[p[0]][p[1]] = "."
    p = (p[0], p[1] - 1)
    m[p[0]][p[1]] = "<"
    return True


#print_map()
res.add(p)
while do_step():
  if p not in res:
    res.add(p)
  #print_map()

print(len(res))
