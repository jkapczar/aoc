res = 0
with open("input.txt", "r") as f:
  for line in f.readlines():
    arr = line.strip().split(" ")
    print(arr)
    first_diff = int(arr[1]) - int(arr[0])
    if first_diff == 0:
      continue
    inc = first_diff > 0
    good = True
    for i in range(0, len(arr) - 1):
      curr_diff = int(arr[i + 1]) - int(arr[i])
      print(curr_diff)
      if not (abs(curr_diff) >= 1 and abs(curr_diff) <= 3 and ((curr_diff < 0 and inc == False) or (curr_diff > 0 and inc == True))):
        good = False
    if good: 
      print("good")
      print("")
      res += 1

print(res)
assert 236 == res
