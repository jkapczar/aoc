cnt = 0

def parse_rounds(rounds):
  current = {"red": 0, "green": 0, "blue": 0}
  for r in rounds:
    if "," in r:
      for g in r.split(","):
        n = int(g.strip().split(" ")[0])
        c = g.strip().split(" ")[1]
        if n > current[c]:
          current[c] = n
        print(f"current: {current}")
    else:
      n = int(r.strip().split(" ")[0])
      c = r.strip().split(" ")[1]
      if n > current[c]:
        current[c] = n
      print(f"current: {current}")
  return current["red"] * current["blue"] * current["green"]

with open("input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    game_num = int(line.split(":")[0].split(" ")[1])
    rounds = line.split(":")[1].strip().split(";")
    res = parse_rounds(rounds)
    print(f"Game: {game_num}, rounds: {rounds}, res: {res}")
    cnt += res
    print(f"answer: {cnt}")

assert cnt == 79315
