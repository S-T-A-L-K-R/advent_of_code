santas_map = {}
x = 0
y = 0

santas_map[(x, y)] = 1

file = open('03.txt', 'rt')
 
while 1:
    char = file.read(1)
    if not char:
        break
    
    if char == '<':
        x -= 1
    elif char == '>':
        x += 1
    elif char == 'v':
        y -= 1
    elif char == '^':
        y += 1
    
    try:
        santas_map[(x, y)] += 1
    except:
        santas_map[(x, y)] = 1
    
print(len(santas_map))