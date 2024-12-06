with open('dVI-input.txt', 'r') as file:
    for line in file:
        grid = [list(line.strip()) for line in file]

rows, cols = len(grid[0]), len(grid)