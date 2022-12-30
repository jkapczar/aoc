import ast

def parse(a, b):
  return [ast.literal_eval(a), ast.literal_eval(b)]

def check(x, y):
  if type(x) == int and type(y) == int:
      if x < y: return -1
      if x == y: return 0
      if x > y: return 1
      
  if type(x) == int:
    x = [x]
  if type(y) == int:
    y = [y]

  for a, b in zip(x, y):
    res = check(a, b)
    if res == 0:
      continue
    return res  
  if len(x) > len(y): return 1
  if len(x) < len(y): return -1
  return 0


arr = []
with open("input.txt", "r") as f:
  for p in f.read().split("\n\n"):
    arr.append(parse(p.split("\n")[0], p.split("\n")[1]))

res = []
for pair in arr:  
  if check(pair[0], pair[1]) == -1:
    res.append(arr.index(pair) + 1)

print(res)
print(sum(res))
