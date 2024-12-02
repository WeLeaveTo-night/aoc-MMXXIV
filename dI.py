from collections import Counter

loc1, loc2 = [], []

with open('dI-input.txt', 'r') as file:
    for line in file:
        l1, l2 = line.split() 
        loc1.append(int(l1))        
        loc2.append(int(l2))

loc1.sort()
loc2.sort()

d = sum(abs(l1 - l2) for l1, l2 in zip(loc1, loc2))

# print(d)

## PART 2
counts = Counter(loc2)

sim_score = 0
for loc in loc1:
    if loc in counts:
        sim_score += counts[loc] * loc

# print(sim_score)