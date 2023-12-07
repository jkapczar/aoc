import sys

def parse_maps(lines):
  map_table = []
  parsing = False
  tmp = []
  for line in lines:
    if "map" in line:
      parsing = True
      continue
    if len(line) == 0:
      parsing = False
      map_table.append(tmp)
      tmp = []
      continue
    if parsing:
      print(line)
      tmp.append(line.split(" "))
  return map_table    


seeds = []
with open(sys.argv[1], "r") as f:
  lines = [line.strip() for line in f.readlines()]
  for line in lines:
    if line.startswith("seeds:"):
      seeds = line.split(":")[1].strip().split(" ")
      print(seeds)
  map_table = parse_maps(lines)
  print(map_table)
