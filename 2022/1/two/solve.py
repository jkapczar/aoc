l = []
current = 0
with open("input.txt", "r") as f:
  for line in f.readlines():
    if len(line) == 1:
      l.append(current)  
      current = 0
    else:
      current += int(line.strip())

l.sort(reverse=True)
print(l[0] + l[1] + l[2])
