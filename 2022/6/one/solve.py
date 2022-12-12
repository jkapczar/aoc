with open("input.txt", "r") as f:
  text = f.read()
  print(text)
  s = 0
  for i in range(len(text)-3):
    tmp = text[s:s+4]
    print(tmp)
    if len(set(tmp)) == 4:
      print(s+4)
      break
    else:
      s += 1
