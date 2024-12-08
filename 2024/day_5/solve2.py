res = 0

rules = []
arr = []
page_map = {}
bad_rows = []

def prepare_cache():
  global rules, page_map
  for r in rules:
    if int(r[0]) not in page_map:
      page_map[int(r[0])] = {int(r[1])}
    else:
      page_map[int(r[0])].add(int(r[1]))

def range_check(arr, v):
  if int(v) not in page_map: return -1
  for index,i in enumerate(arr):
    for j in page_map[v]:
      if int(i) == int(j):
        return index 
  return -1

def row_check():
  global res
  for row in arr:
    print(f"row: {row}")
    add = False
    for i,v in enumerate(row):
      print(f"i: {i}, v: {v}")
      r = range_check(row[0:i+1], int(v))
      if r != -1:
        add = True
        print(f"r: {r}")
        del row[i]
        row.insert(r, v)
        print(f"row: {row}")
    print(f"row: {row}")
    if add: res += int(row[len(row) // 2])


with open("input.txt", "r") as f:
  p2 = False
  for line in f.readlines():
    if not p2 and len(line.strip()) != 0:
      rules.append(line.strip().split("|"))
    if len(line.strip()) == 0:
      p2 = True
      continue
    if p2 and len(line.strip()) != 0:
      arr.append(line.strip().split(","))


prepare_cache()
print(page_map)
row_check()
print(bad_rows)
print(res)
