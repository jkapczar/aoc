with open("input.txt", "r") as f:
  text = f.read()
  print(text)
  s = 0
  for i in range(len(text)-13):
    tmp = text[s:s+14]
    print(tmp)
    if len(set(tmp)) == 14:
      print(s+14)
      break
    else:
      s += 1
