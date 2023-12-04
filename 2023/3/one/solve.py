def create_map(m, arr):
  num = ""
  num_cords = []
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if ord(arr[i][j]) >= 48 and ord(arr[i][j]) <= 57:
        num += arr[i][j]
        num_cords.append([i, j])
      if len(num) > 0 and not (ord(arr[i][j]) >= 48 and ord(arr[i][j]) <= 57):
        if num in m.keys():
          m[num].append(num_cords)
        else:
          m[num] = []
          m[num].append(num_cords)
      
        num = ""
        num_cords = []
  return m

def search(i, j):
  s = []
  for key in [*m]:
    for v in m[key]:
      tmp = set()
      for cord in v:
        if abs(i - cord[0]) <= 1 and abs(j - cord[1]) <= 1:
          tmp.add(int(key))
      s += tmp  
  print(i, j, arr[i][j], s)
  return s

arr = []
m = {}
with open("input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    arr.append(line)

m = create_map(m, arr)
print(m)

res = []
for i in range(len(arr)):
  for j in range(len(arr[i])):
    if not (ord(arr[i][j]) >= 48 and ord(arr[i][j]) <= 57) and arr[i][j] != ".":
      res += search(i, j)

print(res)
answer = sum(res)
print(answer)

assert answer == 535235
