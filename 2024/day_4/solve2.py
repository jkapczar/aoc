res = 0

m = []

def print_arr():
  global m
  [print(r) for r in m]

def check(i, j):
  global m, res
  if (j + 1 < len(m[i]) and j - 1 >= 0 and i + 1 < len(m) and i - 1 >= 0):
    v1 = "".join(m[i-1][j-1] + m[i][j] + m[i+1][j+1])
    v2 = "".join(m[i-1][j+1] + m[i][j] + m[i+1][j-1])
    print(f"i :{i}, j: {j}, v1: {v1}, v2: {v2}")
    if (v1 == "MAS" or v1[::-1] == "MAS") and (v2 == "MAS" or v2[::-1] == "MAS"): res += 1


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
