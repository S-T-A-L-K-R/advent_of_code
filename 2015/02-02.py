
retval = 0
with open('02.txt', 'rt') as file:
    for line in file:
        sides = [int(x) for x in line.split('x')]
        sides.sort()
        c = (sides[0] + sides[1]) * 2
        r = sides[0] * sides[1] * sides[2]
        retval += c + r
print(retval)