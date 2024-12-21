import sys
import itertools

res = set()
grid = []
antenna_dict = {}

def pgrid():
  global grid
  for row in grid:
    print(row)

def parse_grid():
  global grid, antenna_dict
  for i, row in enumerate(grid):
    for j, element in enumerate(row):
      if element != ".":
        if element not in antenna_dict:
          antenna_dict[element] = []
        antenna_dict[element].append((i,j))

def check_boundary(v, p):
  global grid, res
  n = (p[0] + v[0], p[1] + v[1])
  #print(f"v: {v}, p: {p}, n: {n}")
  #print()
  res.add(p)
  if n[0] > -1 and n[0] < len(grid) and n[1] > -1 and n[1] < len(grid[0]):
    res.add(n)
    grid[n[0]][n[1]] = "#"
    check_boundary(v, n)

def generate_node():
  global antenna_dict, grid
  for index, (k, v) in enumerate(antenna_dict.items()):
    print(index, k)
    for p in list(itertools.permutations(v, 2)):
      diff_v = (p[0][0] - p[1][0], p[0][1] - p[1][1])
      #print(p, diff_v)
      check_boundary(diff_v, p[0])
      check_boundary((diff_v[0] * -1, diff_v[1] * -1), p[1])


with open(sys.argv[1], "r") as f:
  for line in f.readlines():
    grid.append(list(line.strip()))

#pgrid()
parse_grid()
print(len(antenna_dict))
generate_node()
#pgrid()
print(len(res))
