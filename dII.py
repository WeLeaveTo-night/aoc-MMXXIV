levels = []

with open('dII-input.txt', 'r') as file:
    for line in file:
        levels.append(list(map(int, line.split())))

safe_lvls = 0 
for l in levels:
    sign = 0
    if l[0] < l[1]:
        sign = 1
    elif l[0] > l[1]:
        sign = -1
    else: 
        continue

    safe = 0
    if sign == 1:
        safe = all(1 <= l[i] - l[i-1] <= 3 for i in range(1, len(l)))
    elif sign == -1:
        safe = all(1 <= l[i-1] - l[i] <= 3 for i in range(1, len(l)))
    safe_lvls += safe

# print(safe_lvls)
    
# PART 2
    pd_safe_lvls = 0

    for l in levels: # only unsafe left
        if (
            sum(1 <= l[i] - l[i-1] <= 3 for i in range(1, len(l))) == len(l)-2
            or 
            sum(1 <= l[i-1] - l[i] <= 3 for i in range(1, len(l))) == len(l)-2
        ):
            pd_safe_lvls += 1

    print(pd_safe_lvls)

