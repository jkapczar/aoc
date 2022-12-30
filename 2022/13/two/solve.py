import ast
from functools import cmp_to_key

def parse(a):
  return [ast.literal_eval(a)]

def cmp(x, y):
  if type(x) == int and type(y) == int:
      if x < y: return -1
      if x == y: return 0
      if x > y: return 1
      
  if type(x) == int:
    x = [x]
  if type(y) == int:
    y = [y]

  for a, b in zip(x, y):
    res = cmp(a, b)
    if res == 0:
      continue
    return res  
  if len(x) > len(y): return 1
  if len(x) < len(y): return -1
  return 0

arr = []
with open("input.txt", "r") as f:
  for p in f.read().split("\n\n"):
    arr += [parse(p.split("\n")[0]), parse(p.split("\n")[1])]

arr.append([[2]])
arr.append([[6]])

sorted_l = sorted(arr, key=cmp_to_key(cmp))

print(sorted_l)
print((sorted_l.index([[2]]) + 1)  * (sorted_l.index([[6]]) + 1))
