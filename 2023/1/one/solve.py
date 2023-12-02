s = 0
with open("input.txt", "r") as f:
  for line in f.readlines():
    arr = [c for c in line.strip() if ord(c) >= 48 and ord(c) <= 57]
    s += int(arr[0] + arr[-1])
    print(s)

assert 54561 == s
