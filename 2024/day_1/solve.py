l1 = []
l2 = []

with open('input.txt', 'r') as f:
  for line in f.readlines():
    l_arr = line.split("   ")
    l1.append(l_arr[0].strip())
    l2.append(l_arr[1].strip())


l1_sorted = sorted(l1)
l2_sorted = sorted(l2)

res = 0

for i in range(0, len(l1)):
  res += abs(int(l1_sorted[i]) - int(l2_sorted[i]))

print(res)
assert res == 2066446 
