import sys

res = 0
data = []

def extract(v):
  global data
  ID = 0
  for index, num in enumerate(v):
    if index % 2 == 0:
      for i in range(int(num)):
        data.append(ID)
      ID += 1
    else:
      for i in range(int(num)):
        data.append(-1)
  #print(data)    
  rearrange()

def rearrange():
  global data
  left_index = 0
  right_index = len(data) - 1
  while True:
    while data[left_index] != -1:
      left_index += 1
    while data[right_index] == -1:
      right_index -= 1
    if left_index > right_index: break
    #print(f"l_i: {left_index}, r_i: {right_index}, data[l_i]: {data[left_index]}, data[r_i]: {data[right_index]}")  
    data[left_index] = data[right_index]
    data[right_index] = -1
    #print(data)
  sum_res()  

def sum_res():
  global data, res
  index = 0
  while data[index] != -1:
    res += index * data[index]
    index += 1
  print(res)

with open(sys.argv[1], "r") as f:
  for line in f.readlines():
    extract(line.strip())  
