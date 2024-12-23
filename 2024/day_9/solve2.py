import sys

res = 0
data = []

def extract(v):
  global data
  ID = 0
  if len(v) % 2 != 0: v += "0"
  for index in range(0, len(v) - 1, 2):
    data.append([ID, int(v[index]), int(v[index + 1]), 0])
    ID += 1
  #print(data)    
  rearrange()

def rearrange():
  global data
  right_index = len(data) - 1
 
  while True:
    if right_index < 0: break
    #already updated
    if data[right_index][3] == 1: 
      right_index -= 1
      continue
    
    for left_index in range(0, right_index):
      #print(left_index, right_index)
      #free space bigger or equal to size
      if data[right_index][1] <= data[left_index][2]:
        #print(f"l_i: {left_index}, r_i: {right_index}, data[l_i]: {data[left_index]}, data[r_i]: {data[right_index]}")  
        #set was updated
        data[right_index][3] = 1
        #recalculate free speace from right before moving
        data[right_index - 1][2] = data[right_index - 1][2] + data[right_index][1] + data[right_index][2]
        #recalculate free space on left
        data[right_index][2] = data[left_index][2] - data[right_index][1]
        #when merging left and right any free space left on left side gose on right inserted
        data[left_index][2] = 0
        #insert to new place
        data.insert(left_index + 1, data[right_index])
        #remove from old place
        data = data[:right_index+1] + data[right_index+2:]
        #print(data)
        #print()
        #becase we moved data[right_index] and inserted to left_index + 1 -> right_index is a new value so we need to check again
        right_index += 1
        break
    
    right_index -= 1
  sum_res()  

def sum_res():
  global data, res
  partial_res = []
  for v in data:
    for i in range(v[1]): partial_res.append(v[0])
    for i in range(v[2]): partial_res.append(-1)
  
  for index in range(len(partial_res)):
    if partial_res[index] != -1:
      res += index * partial_res[index]
  print(res)

with open(sys.argv[1], "r") as f:
  for line in f.readlines():
    extract(line.strip())  
