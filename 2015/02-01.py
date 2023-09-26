
retval = 0
with open('02.txt', 'rt') as file:
    for line in file:
        sides = [int(x) for x in line.split('x')]
        sides.sort()
        area = 3 * sides[0] * sides[1] +\
            2 * sides[0] * sides[2] +\
            2 * sides[1] * sides[2]
        retval += area
print(retval)