cnt = 0
available = {"red": 12, "green": 13, "blue": 14}

def check_round(game_round):
  for key in [*available]:
    if game_round[key] > available[key]:
      return False
  return True


def parse_rounds(rounds):
  for r in rounds:
    current = {"red": 0, "green": 0, "blue": 0}
    if "," in r:
      for g in r.split(","):
        n = int(g.strip().split(" ")[0])
        c = g.strip().split(" ")[1]
        current[c] += n
        res = check_round(current)
        print(f"current: {current}, res: {res}")
        if res == False: return False
    else:
      n = int(r.strip().split(" ")[0])
      c = r.strip().split(" ")[1]
      current[c] += n
      res = check_round(current)
      print(f"current: {current}, res: {res}")
      if res == False: return False
  return True

with open("input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    game_num = int(line.split(":")[0].split(" ")[1])
    rounds = line.split(":")[1].strip().split(";")
    res = parse_rounds(rounds)
    print(f"Game: {game_num}, rounds: {rounds}, res: {res}")
    if res: cnt += game_num
    print(f"answer: {cnt}")

assert 2085 == cnt

