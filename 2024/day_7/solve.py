import sys
from itertools import product

res = 0
operators = ["*", "+"]

def do_operation(op, partial_res, num):
  if "*" == op: return partial_res * num
  if "+" == op: return partial_res + num

with open(sys.argv[1], "r") as f:
  for index, line in enumerate(f.readlines()):
    print(index)
    data = line.strip().split(":")
    result = int(data[0].strip())
    nums = list(map(int, data[1].strip().split()))
    #print(result, nums)
    generated_ops = list(product(operators, repeat=len(nums) - 1))
    #print(generated_ops)
    for ops in generated_ops:
      
      #print(f"ops: {ops}")
      partial_res = nums[0]  
      
      for index in range(len(nums) - 1):
        #print(f"ops: {ops[index]}, partial_res: {partial_res}, nums[index+1]: {nums[index+1]}")
        partial_res = do_operation(ops[index], partial_res, nums[index+1])
        #print(partial_res)
        if partial_res > result: break
      
      if partial_res == result: 
        res += result
        break


print(res)
