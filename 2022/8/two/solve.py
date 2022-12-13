def checkTop(data, i, j):
  cnt = 0
  for x in range(i-1, -1, -1):
    cnt += 1
    if data[i][j] <= data[x][j]:
      print(f"TOP {cnt}")
      return cnt
  return cnt

def checkBottom(data, i, j):
  cnt = 0
  for x in range(i+1, len(data)):
    cnt += 1
    if data[i][j] <= data[x][j]:
      print(f"BOTTOM {cnt}")
      return cnt
  return cnt

def checkRight(data, i, j):
  cnt = 0
  for x in range(j+1, len(data[i])):
    cnt += 1
    if data[i][j] <= data[i][x]:
      print(f"RIGHT {cnt}")
      return cnt
  return cnt

def checkLeft(data, i, j):
  cnt = 0
  for x in range(j-1, -1, -1):
    cnt += 1
    if data[i][j] <= data[i][x]:
      print(f"LEFT {cnt}")
      return cnt
  return cnt

data = []
with open("input.txt", "r") as f:
  for line in f.readlines():
    data.append(line.strip())

curr_max = 0
for i in range(1, len(data)-1):
  for j in range(1, len(data[i])-1):
    tmp = checkTop(data, i, j) * checkBottom(data, i, j)  * checkRight(data, i, j)  * checkLeft(data, i, j)
    print(data[i][j], i, j, curr_max)
    if curr_max < tmp:
      curr_max = tmp
     

print(curr_max)  
