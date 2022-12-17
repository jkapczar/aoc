moves = []
c_head_poz = [0, 0]
p_head_poz = [0, 0]
tail_poz = [0, 0]
unique_poz = set()
unique_poz.add("00")

with open("input.txt", "r") as f:  
  for line in f.readlines():
    moves.append(line.strip().split(" "))

def update_tail(direction, c_head_poz, p_head_poz, tail_poz):
  print(f"update_tail: direction {direction}, current head: {c_head_poz}, prev head: {p_head_poz},  current tail: {tail_poz}")
  if abs(c_head_poz[0] - tail_poz[0]) > 1 or abs(c_head_poz[1] - tail_poz[1]) > 1:
    print("tail needs to be updated")
    tail_poz = [p_head_poz[0], p_head_poz[1]]
    unique_poz.add("".join(map(str, tail_poz)))
  return tail_poz
   
for move in moves:
  direction = move[0]
  length = int(move[1])
  for step in range(length):
    p_head_poz = [c_head_poz[0], c_head_poz[1]]
    if direction == 'R':
      c_head_poz[0] += 1
    elif direction == 'U':
      c_head_poz[1] += 1
    elif direction == 'D':
      c_head_poz[1] -= 1
    else:
      c_head_poz[0] -= 1
    tail_poz = update_tail(direction, c_head_poz, p_head_poz, tail_poz)


print(unique_poz)
print(len(unique_poz))
