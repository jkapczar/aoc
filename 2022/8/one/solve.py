def checkTop(data, i, j):
  for x in range(i-1, -1, -1):
    if data[i][j] <= data[x][j]:
      return False
  print("TOP")
  return True

def checkBottom(data, i, j):
  for x in range(i+1, len(data)):
    if data[i][j] <= data[x][j]:
      return False    
  print("BOTTOM")
  return True


def checkRight(data, i, j):
  for x in range(j+1, len(data[i])):
    if data[i][j] <= data[i][x]:
      return False
  print("RIGHT")
  return True


def checkLeft(data, i, j):
  for x in range(j-1, -1, -1):
    if data[i][j] <= data[i][x]:
      return False
  print("LEFT")
  return True

data = []
with open("input.txt", "r") as f:
  for line in f.readlines():
    data.append(line.strip())

base = (2 * len(data) + 2 * len(data[0])) -4
print(f"base {base}")


cnt = 0
for i in range(1, len(data)-1):
  for j in range(1, len(data[i])-1):
    if checkTop(data, i, j) or checkBottom(data, i, j)  or checkRight(data, i, j)  or checkLeft(data, i, j):
      print(data[i][j], i, j)
      cnt += 1
     

print(base + cnt)  
