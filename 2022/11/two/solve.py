import math

arr = []
d = {}
with open("input.txt", "r") as f:
  for i in f.read().split("\n\n"):
    arr.append(i)

#parse
for i in arr:
  l_arr = i.split("\n")
  m_num = int(l_arr[0].split(" ")[1][:1])
  print(f"m_num: {m_num}")
  items = l_arr[1].split(":")[1].strip().split(", ")
  items = [int(x) for x in items]
  print(f"items: {items}")
  op = l_arr[2].split("=")[1].strip()
  print(f"op: {op}")
  divisible = int(l_arr[3].split("by")[1].strip())
  print(f"divisible: {divisible}")
  true_op = int(l_arr[4].strip().split(" ")[5])
  print(f"true_op: {true_op}")
  false_op = int(l_arr[5].strip().split(" ")[5])
  print(f"false_op: {false_op}")
  ins_num = 0
  d[m_num] = [items, op, divisible, true_op, false_op, ins_num]

print(d)

div_arr = [v[2] for v in d.values()]
mod = math.prod(div_arr)

def do_operation(old_value: int, operation: str) -> int:
  op = operation.split(" ")[1]
  v = operation.split(" ")[2]
  if v == 'old': v = old_value
  v = int(v)
  if op == '+':
    return (old_value + v) % mod
  elif op == '-':
    return (old_value - v) % mod
  elif op == '*':
    return (old_value * v) % mod
  else:
    return (old_value / v) % mod


def do_test(value: int, divisible: int) -> bool:
  return value % divisible == 0


for r in range(10000):
  print(r)
  for k, v in d.items():
    for i in v[0]:
      new_value = do_operation(i, v[1])
      v[5] += 1
      if do_test(new_value, v[2]):
        d[v[3]][0].append(new_value)
      else:
        d[v[4]][0].append(new_value)
    d[k][0] = []


print(d)


tmp = [v[5] for v in d.values()]
tmp.sort(reverse = True)
print(tmp)
print(tmp[0] * tmp[1])
