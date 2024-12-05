from collections import defaultdict

with open('dV-input.txt', 'r') as file:
    for line in file:
        data = file.readlines()

ords_raw = [tuple(map(int, line.split('|'))) for line in data if '|' in line]
updates = [list(map(int, line.split(','))) for line in data if ',' in line]

orders = defaultdict(list)

for k,v in ords_raw:
    orders[k].append(v)

def is_order_correct(update):
    for i, page in enumerate(update):
        for j in range(i+1, len(update)):
            if update[j] in orders[page] and update[j] > page:
                return False
    return True

mids_sum = 0
for update in updates:
    mids_sum += update[len(update) // 2] if is_order_correct else 0

print(mids_sum)