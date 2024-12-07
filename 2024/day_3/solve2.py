import re

res = 0

def sum_muls(text):
  print(text)
  global res
  mathes = re.findall("mul\(\d{1,3},\d{1,3}\)", text.strip())
  for m in mathes:
    print(f"m: {m}")
    r = m.split("(")[1].split(",")
    print(f"r: {r}")
    a = int(r[0])
    print(f"a: {a}")
    b = int(r[1][:-1])
    print(f"b: {b}")
    res += (int(a) * int(b))

with open("input.txt", "r") as f:
  for line in f.readlines():
    for i, v in enumerate(line.split("don't()")):
      if i == 0: 
        sum_muls(v)
        continue
      try:
        index = v.index("do()")
        sum_muls(v[index:])
      except Exception:
        pass
        
print(res)
assert 98729041 == res
