res = 0

m = []

def print_arr():
  global m
  [print(r) for r in m]

def check(i, j):
  global m, res
  if (j + 3 < len(m[i])): 
    v = "".join(m[i][j] + m[i][j+1] + m[i][j+2] + m[i][j+3])
    print(f"v: {v} i: {i}, j: {j}, direction: RIGHT")
    if v == "XMAS": res += 1
  if (j - 3 >= 0):
    v = "".join(m[i][j] + m[i][j-1] + m[i][j-2] + m[i][j-3])
    print(f"v: {v} i: {i}, j: {j}, direction: LEFT")
    if v == "XMAS": res += 1
  if (i + 3 < len(m)):
    v = "".join(m[i][j] + m[i+1][j] + m[i+2][j] + m[i+3][j])
    print(f"v: {v} i: {i}, j: {j}, direction: DOWN")
    if v == "XMAS": res += 1
  if (i - 3 >= 0):
    v = "".join(m[i][j] + m[i-1][j] + m[i-2][j] + m[i-3][j])
    print(f"v: {v} i: {i}, j: {j}, direction: UP")
    if v == "XMAS": res += 1
  if (j + 3 < len(m[i]) and  i - 3 >= 0):
    v = "".join(m[i][j] + m[i-1][j+1] + m[i-2][j+2] + m[i-3][j+3])
    print(f"v: {v} i: {i}, j: {j}, direction: UP_RIGHT")
    if v == "XMAS": res += 1
  if (j - 3 >= 0 and  i - 3 >= 0):
    v = "".join(m[i][j] + m[i-1][j-1] + m[i-2][j-2] + m[i-3][j-3])
    print(f"v: {v} i: {i}, j: {j}, direction: UP_LEFT")
    if v == "XMAS": res += 1
  if (j - 3 >= 0 and  i + 3 < len(m)):
    v = "".join(m[i][j] + m[i+1][j-1] + m[i+2][j-2] + m[i+3][j-3])
    print(f"v: {v} i: {i}, j: {j}, direction: DOWN_LEFT")
    if v == "XMAS": res += 1
  if (j + 3 < len(m[i]) and  i + 3 < len(m)):
    v = "".join(m[i][j] + m[i+1][j+1] + m[i+2][j+2] + m[i+3][j+3])
    print(f"v: {v} i: {i}, j: {j}, direction: DOWN_RIGHT")
    if v == "XMAS": res += 1
 
def traverse_and_count():
  global m
  for i in range(0, len(m)):
    for j in range(0, len(m[i])):
      check(i, j)
        

with open("input.txt", "r") as f:
  for line in f.readlines():
    m.append(list(line.strip()))

print_arr()
traverse_and_count()
print(f"res: {res}")
assert 2573 == res
