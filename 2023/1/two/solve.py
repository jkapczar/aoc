s = 0
nums = {"one": '1', "two": '2', "three": '3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9', "zero":'0'}

def find_num(text, rev):
  for i in range(len(text)):
    
    if ord(text[i]) >= 48 and ord(text[i]) <= 57:
      print(f"num found {text[i]}")
      return str(text[i])
    
    for key in [*nums]:
      if key in text[0:i+1] or (rev and key[::-1] in text[0:i+1]):
        print(f"num key found {nums[key]}")
        return str(nums[key])

with open("input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    
    l = find_num(line, False)
    print(line[::-1])
    
    r = find_num(line[::-1], True)
    print(f"left: {l}, right: {r}")
    
    s += int(l + r)
    print(s)
