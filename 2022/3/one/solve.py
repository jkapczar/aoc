import string
cnt = 0
with open("input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    found = False
    for c1 in line[0:len(line)//2]:
      for c2 in line[len(line)//2:len(line)]:  
        if c1 == c2:
          found = True
          if c1 in string.ascii_lowercase:
            cnt += string.ascii_lowercase.index(c1) + 1
          else:
            cnt += 26 + string.ascii_uppercase.index(c1) + 1
          break
      if found: break
print(cnt)
