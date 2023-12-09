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
    if line == lines[-1]:
      tmp.append(line.split(" "))
      map_table.append(tmp)
      continue
    if parsing:
      tmp.append(line.split(" "))
  return map_table[1:]

def mapping(seed, map_entry):
  for entry in map_entry:
    destination = int(entry[0])
    source = int(entry[1])
    m_range = int(entry[2])
    seed = int(seed)
    print(f"destination: {destination}, source: {source}, m_range: {m_range}")
    left = source
    right = source + m_range - 1
    if seed >= left and seed <= right:
      tmp = right - seed
      result = destination + m_range - tmp - 1
      print(f"found: {seed}, mapped: {result}")
      return result
  return seed

seeds = []
with open(sys.argv[1], "r") as f:
  lines = [line.strip() for line in f.readlines()]
  for line in lines:
    if line.startswith("seeds:"):
      seeds = line.split(":")[1].strip().split(" ")
      print(seeds)
  map_table = parse_maps(lines)
  print(f"map_table: {map_table}")
  results = []
  for seed in seeds:
    current_form_of_seed = seed
    for map_entry in map_table:
      print(f"current_form_of_seed: {current_form_of_seed}, map_entry: {map_entry}")
      current_form_of_seed = mapping(current_form_of_seed, map_entry)
    results.append(current_form_of_seed)
    print(f"r: {current_form_of_seed}")
  print(f"res: {results}")
  print(f"res: {min(results)}")
  assert 551761867 == min(results)
