import re

with open('dIII-input.txt', 'r') as file:
    mem = file.read() 

muls = re.findall('mul\((\d+),(\d+)\)', mem)

sum_muls = sum(int(x) * int(y) for x, y in muls)

# print(sum_muls)

# PART 2 

# cmds = re.findall('(mul|do|don\'t)\((?:\d+)(?:,(\d+)\))', mem)
cmds = re.findall('(do)\(\)|(mul)\((\d+),(\d+)\)?', mem)
b = re.findall(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', mem)
do = True 
