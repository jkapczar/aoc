cnt = 0
with open("input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    f = line.split(",")[0]
    s = line.split(",")[1]
    f1 = int(f.split("-")[0])
    f2 = int(f.split("-")[1])
    s1 = int(s.split("-")[0])
    s2 = int(s.split("-")[1])
    if (f1 in range(s1, s2+1) or f2 in range(s1, s2+1)) or (s1 in range(f1, f2+1) or s2 in range(f1, f2+1)):
      cnt += 1
print(cnt)
