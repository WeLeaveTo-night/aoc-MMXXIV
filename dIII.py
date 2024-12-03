import re

with open('dIII-input.txt', 'r') as file:
    mem = file.read() 

muls = re.findall('mul\((\d+),(\d+)\)', mem)

sum_muls = sum(int(x) * int(y) for x, y in muls)

# print(sum_muls)

# PART 2 

cmds = re.findall('(do)\(\)|(mul)\((\d+),(\d+)\)?', mem)

do = True 
