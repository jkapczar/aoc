res = 0

def test(arr):
  print(f"arr: {arr}, len(arr): {len(arr)}")
  diff_arr = []
  for i in range(0, len(arr) - 1):
    diff = arr[i+1] - arr[i]
    diff_arr.append(diff)
    print(f"diff: {diff}")
    if not (abs(diff) >= 1 and abs(diff) <= 3):
      return False
  print(f"diff_arr: {diff_arr}")
  return all(x > 0 for x in diff_arr) or all(x < 0 for x in diff_arr)

with open("input.txt", "r") as f:
  for line in f.readlines():
    arr = [int (x) for x in line.strip().split(" ")]
    if test(arr): 
      print("good")
      res += 1
    else:
      print("bad")
    print()  

print(res)
assert 236 == res
