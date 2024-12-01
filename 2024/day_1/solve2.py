l1 = []
l2 = []

cache = {}
res = 0

with open('input.txt', 'r') as f:
  for line in f.readlines():
    l_arr = line.split("   ")
    l1.append(int(l_arr[0].strip()))
    l2.append(int(l_arr[1].strip()))

for i in range(0, len(l1)):
  if l1[i] in cache:
    res += cache[l1[i]]
  else:
    occurrence = 0
    for j in range(0, len(l2)):
      if l2[j] == l1[i]:
        occurrence += 1
    part_res = occurrence * l1[i]
    res += part_res
    cache[l1[i]] = part_res

print(res)
#assert res == 2066446 
