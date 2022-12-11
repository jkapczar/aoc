max = 0
current = 0
with open("input.txt", "r") as f:
  for line in f.readlines():
    if len(line) == 1:
      if current > max:
        max = current
        current = 0
      else:
        current = 0
    else:
      current += int(line.strip())

print(max)
