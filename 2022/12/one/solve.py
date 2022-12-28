from string import ascii_lowercase

class Node:
  def __init__(self, poz, parent, children, path, char):
    self.poz = poz
    self.parent = parent
    self.children = children
    self.path = path
    self.char = char

  def __repr__(self):
    if self.parent != None:
      return f"poz: {self.poz}; parent: {self.parent.poz}; path: {self.path}; char: {self.char}"
    else:
      return f"poz: {self.poz}; parent: None; path: {self.path}; char: {self.char}"
  
  def explore(self, m):
    x = self.poz[0]
    y = self.poz[1]
    self.path.append(self.poz)
    if x + 1 < len(m[0]) and self.valid_step(x+1, y, m):
      self.children.append(Node((x+1, y), self, [], self.path.copy(),  m[y][x+1]))
    if x - 1 > -1 and self.valid_step(x-1, y, m):
      self.children.append(Node((x-1, y), self, [], self.path.copy(),  m[y][x-1]))
    if y + 1 < len(m) and self.valid_step(x, y+1, m):
      self.children.append(Node((x, y+1), self, [], self.path.copy(), m[y+1][x]))
    if y - 1 > -1 and self.valid_step(x, y-1, m):
      self.children.append(Node((x, y-1), self, [], self.path.copy(), m[y-1][x]))
    return self.children

  def valid_step(self, x, y, m):
    d = Node.dept_in_ascii(m[y][x]) - Node.dept_in_ascii(self.char)
    return d < 2
  
  @classmethod
  def dept_in_ascii(self, char):
    if char == "S": char = 'a'
    if char == "E": char = 'z'
    return ascii_lowercase.index(char.strip())


m = []
with open("input.txt", "r") as f:
  for line in f.readlines():
    m.append(line.strip())


start = None
for i in range(len(m)):
  for j in range(len(m[i])):
    if m[i][j] == 'S':
      start = (j,i)

print(start)

visited = [start]
queue = []
node = Node(start, None, [], [], 'a')
node.explore(m)
queue += node.children

while len(queue) > 0:
  node = queue.pop(0)
  if node.char == 'E':
    print(f"FOUND steps: {len(node.path)}")
    print(f"FOUND steps: {node.path}")
    break
  if node.poz not in visited:
    visited.append(node.poz)
    queue += node.explore(m)
