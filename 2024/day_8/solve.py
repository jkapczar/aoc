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

def check_boundary(v, p1, p2):
  global grid, res
  n1 = (p1[0] + v[0], p1[1] + v[1])
  n2 = (p2[0] - v[0], p2[1] - v[1])
  #print(f"v: {v}, p1: {p1}, p2: {p2}, n1: {n1}, n2: {n2}")
  #print()
  if n1[0] > -1 and n1[0] < len(grid) and n1[1] > -1 and n1[1] < len(grid[0]):
    res.add(n1)
    grid[n1[0]][n1[1]] = "#"
  if n2[0] > -1 and n2[0] < len(grid) and n2[1] > -1 and n2[1] < len(grid[0]):
    res.add(n2)
    grid[n2[0]][n2[1]] = "#"


def generate_node():
  global antenna_dict, grid
  for k, v in antenna_dict.items():
    for p in list(itertools.permutations(v, 2)):
      diff_v = (p[0][0] - p[1][0], p[0][1] - p[1][1])
      #print(p, diff_v)
      check_boundary(diff_v, p[0], p[1])


with open(sys.argv[1], "r") as f:
  for line in f.readlines():
    grid.append(list(line.strip()))

#pgrid()
parse_grid()
generate_node()
#pgrid()
print(len(res))
