data = {}
def parseTree(path, command):
  print(f"CURRENT PATH {path}")
  if command == "$ cd /":
    print("create root node /")
    path = path + "/"
    data[path] = 0
  elif command == "$ cd ..":
    path = "/".join(path.split("/")[:-2]) + '/'
    print(f"step back to {path}")
  elif command.startswith("$ cd"):
    path += command.split(" ")[2] + '/'
    data[path] = 0
    print(f"go to directory {path}")
  elif command == "$ ls":
    print("listing directory")
  else:
    print(f"element: {command}")
    if not command.startswith("dir"):
      data[path] += int(command.split(" ")[0])
      print(f"updated path size: {data[path]}")
  return path

path = ""
with open("input.txt", "r") as f:
  for line in f.readlines():
    path = parseTree(path, line.strip())


for k in sorted(data.keys(), reverse=True):
  for k1,v1 in data.items():  
    if k != k1 and k == ("/".join(k1.split("/")[:-2]) + '/'):
      data[k] += v1
      
full = 70000000
have = data["/"]
print(full, have, full-have)

sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))
for k,v in sorted_dict.items():
  if (full - have + v > 30000000):
    print(k,v)
    break

