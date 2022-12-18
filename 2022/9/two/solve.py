moves = []
poz = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
unique_poz = set()
unique_poz.add("0,0")

with open("input.txt", "r") as f:  
  for line in f.readlines():
    moves.append(line.strip().split(" "))

def update_poz_list(poz):
  print("update poz list")
  for c_poz in range(len(poz) - 1):
    print(f"poz: {poz}")
    dx = poz[c_poz][0] - poz[c_poz + 1][0]
    dy = poz[c_poz][1] - poz[c_poz + 1][1]

    if dx > 1 and dy == 0:
      poz[c_poz + 1][0] += 1
    elif dx < -1 and dy == 0:
      poz[c_poz + 1][0] -= 1
    elif dx == 0 and dy > 1:
      poz[c_poz + 1][1] += 1
    elif dx == 0 and dy < -1:
      poz[c_poz + 1][1] -= 1
    elif (dx > 0 and dy > 1) or (dx > 1 and dy > 0):
      poz[c_poz + 1][0] += 1
      poz[c_poz + 1][1] += 1
    elif (dx > 0 and dy < -1) or (dx > 1 and dy < 0):
      poz[c_poz + 1][0] += 1
      poz[c_poz + 1][1] -= 1
    elif (dx < 0 and dy > 1) or (dx < -1 and dy > 0):
      poz[c_poz + 1][0] -= 1
      poz[c_poz + 1][1] += 1
    elif (dx < 0 and dy < -1) or (dx < -1 and dy < 0):
      poz[c_poz + 1][0] -= 1
      poz[c_poz + 1][1] -= 1
      
    print(f"poz: {poz}")
    print("")
  unique_poz.add(",".join(map(str, poz[9])))
  return poz
   
for move in moves:
  direction = move[0]
  length = int(move[1])
  for step in range(length):
    if direction == 'R':
      poz[0] = [poz[0][0] + 1, poz[0][1]]
    elif direction == 'U':
      poz[0] = [poz[0][0], poz[0][1] + 1]
    elif direction == 'D':
      poz[0] = [poz[0][0], poz[0][1] - 1]
    else:
      poz[0] = [poz[0][0] - 1, poz[0][1]]
    poz = update_poz_list(poz)

print(unique_poz)
print(len(unique_poz))
