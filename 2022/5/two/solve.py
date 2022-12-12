text = ""
l1 = []
l2 = []
with open("test.txt", "r") as f:
  text = f.read()

for i in text.split("\n\n")[0].split("\n"):
   l1.append(i[1::4])

l1 = l1[:-1]
l1.reverse()
for i in range(len(l1)+1):
  l2.append([j[i] for j in l1 if j[i] != ' '])

l1 = []
for i in text.split("\n\n")[1].split("\n"):
   l = i.split(" ")
   if len(l) > 1: l1.append([l[1], l[3], l[5]])


for move in l1:
  size = int(move[0])
  source = int(move[1])
  target = int(move[2])
  a = l2[source-1][-size:]
  #a.reverse()
  print("move", size, source, target, a)
  l2[source-1] = l2[source-1][0:-size]
  l2[target-1] = l2[target-1] + a
  print(l2)

print("".join([i[len(i)-1] for i in l2]))
