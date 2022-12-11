import string
lines = []
cnt = 0
with open("input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    lines.append(line)

def find_char(l1, l2, l3):
  for i in l1:
    if i in l2 and i in l3:
      return i

for i in range(0, len(lines), 3):
  c = find_char(lines[i], lines[i+1], lines[i+2])
  if c in string.ascii_lowercase:
    cnt += string.ascii_lowercase.index(c) + 1
  else:
    cnt += 26 + string.ascii_uppercase.index(c) + 1


print(cnt)
