terms = []

with open('dVII-input.txt', 'r') as file:
    for line in file: 
        raw =  line.strip().split(':')
        raw[1] = raw[1].strip().split(' ')
        terms.append(raw)
