import sys

def parse_maps(lines):
  map_table = []
  parsing = False
  tmp = []
  for line in lines:
    if "map" in line:
      print(line)
      parsing = True
      continue
    if len(line) == 0:
      parsing = False
      map_table.append(tmp)
      tmp = []
      continue
    if line == lines[-1]:
      tmp.append(line.split(" "))
      map_table.append(tmp)
      continue
    if parsing:
      tmp.append(line.split(" "))
  return map_table[1:]

def mapping(s, e):
  for m in e:
    des = int(m[0])
    sor = int(m[1])
    ran = int(m[2])
    print(f"des: {des}, sor: {sor}, ran: {ran}")
    try:
      v = list(range(sor, sor + ran)).index(int(s))
      r = list(range(des, des + ran))[v]
      print(f"found: {s}, mapped: {r}")
      return r
    except ValueError:
      print(f"not found: {s}")
  return s

seeds = []
with open(sys.argv[1], "r") as f:
  lines = [line.strip() for line in f.readlines()]
  for line in lines:
    if line.startswith("seeds:"):
      seeds = line.split(":")[1].strip().split(" ")
      print(seeds)
  map_table = parse_maps(lines)
  print(f"map_table: {map_table}")
  res = []
  for s in seeds:
    r = s
    for e in map_table:
      print(f"seed: {r}, entry: {e}")
      r = mapping(r, e)
    res.append(r)
    print(f"r: {r}")
  print(f"res: {res}")
  print(f"res: {min(res)}")
