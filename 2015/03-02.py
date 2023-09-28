santas_map = {}
x1 = 0
y1 = 0
x2 = 0
y2 = 0
santas_map[(x1, y1)] = 1
santas_map[(x2, y2)] = 1

file = open('03.txt', 'rt')
 
while 1:
    char = file.read(1)
    if not char:
        break
    
    if char == '<':
        x1 -= 1
    elif char == '>':
        x1 += 1
    elif char == 'v':
        y1 -= 1
    elif char == '^':
        y1 += 1
    
    try:
        santas_map[(x1, y1)] += 1
    except:
        santas_map[(x1, y1)] = 1
    
    char = file.read(1)
    if not char:
        break
    
    if char == '<':
        x2 -= 1
    elif char == '>':
        x2 += 1
    elif char == 'v':
        y2 -= 1
    elif char == '^':
        y2 += 1
    
    try:
        santas_map[(x2, y2)] += 1
    except:
        santas_map[(x2, y2)] = 1

print(len(santas_map))