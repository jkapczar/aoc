ssp = [20, 60, 100, 140, 180, 220]
x = 1
c = 1
v = []

def update_v(c, x, v):
  for i in ssp:
    if c == i:
      print(c, x, i*x)
      v.append(i*x)
  return v

with open("input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    if line == 'noop':
      c += 1
      v = update_v(c, x, v)
    else:
      c += 1
      v = update_v(c ,x, v)
      x += int(line.split(" ")[1])
      c += 1
      v = update_v(c, x, v)

print(sum(v))

