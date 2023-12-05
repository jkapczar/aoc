res = []
with open("input.txt", "r") as f:
  lines = [line.strip() for line in f.readlines()]
  for line in lines:
    winning_nums = line.split(":")[1].strip().split("|")[0].strip().replace("  ", " ").split(" ")
    my_nums = line.split(":")[1].strip().split("|")[1].strip().replace("  ", " ").split(" ")
    print(winning_nums) 
    print(my_nums)
    print("------------")
    
    m = []
    for my_num in my_nums:
      for w_num in winning_nums:
        if int(my_num) == int(w_num):
          m.append(my_num)
    print(f"matches: {m}")
    if len(m) == 0: 
      res.append(0)
    elif len(m) == 1:
      res.append(1)
    else: 
      res.append(2**(len(m) - 1))
    print(f"res: {res}")
print(sum(res))
assert sum(res) == 21105
