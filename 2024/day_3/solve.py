import re

res = 0

with open("input.txt", "r") as f:
  for line in f.readlines():
    mathes = re.findall("mul\(\d{1,3},\d{1,3}\)", line.strip())
    for m in mathes:
      print(f"m: {m}")
      r = m.split("(")[1].split(",")
      print(f"r: {r}")
      a = int(r[0])
      print(f"a: {a}")
      b = int(r[1][:-1])
      print(f"b: {b}")
      res += (int(a) * int(b))

print(res)
assert 181345830 == res
