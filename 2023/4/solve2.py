tmp = {}
res = 0
with open("input.txt", "r") as f:
  lines = [line.strip() for line in f.readlines()]
  
  for i in range(1, len(lines) + 1):
    tmp[i] = 1

  for line in lines:
    card_num = int(line.split(":")[0].strip().split(" ")[-1].strip())
    winning_nums = line.split(":")[1].strip().split("|")[0].strip().replace("  ", " ").split(" ")
    my_nums = line.split(":")[1].strip().split("|")[1].strip().replace("  ", " ").split(" ")
    print(f"card_num: {card_num}, instances: {tmp[card_num]}  winning_nums: {winning_nums}, my_nums: {my_nums}") 
    print("------------")
    
    m = []
    for my_num in my_nums:
      for w_num in winning_nums:
        if int(my_num) == int(w_num):
          m.append(my_num)
    print(f"matches: {m}, len: {len(m)}")
    for i in range(card_num + 1, card_num + 1 + len(m)):
      tmp[i] += tmp[card_num]

for key in [*tmp]:
  res += tmp[key]
print(f"res: {res}")
assert res == 5329815
