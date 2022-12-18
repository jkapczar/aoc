res = []
s_poz = 2
c = 1
c_line = []

def update_v(c, s_poz, c_line):
  if s_poz == c or s_poz - 1 == c or s_poz + 1 == c:
    c_line.append("#")
  else:
    c_line.append(".")

  if c == 40:
    res.append(c_line)
    c_line = []
    c = 1
  else:
    c += 1
  
  return c_line, c

with open("input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    #print(f"line: {line}, c: {c}, s_poz: {s_poz}, c_line: {''.join(c_line)}")
    if line == 'noop':
      c_line, c = update_v(c, s_poz, c_line)
    else:
      c_line, c = update_v(c, s_poz, c_line)
      c_line, c = update_v(c, s_poz, c_line)
      s_poz += int(line.split(" ")[1])

for i in res:
  print("".join(i))

