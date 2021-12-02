listfile = 'Dec 2\Dec 2 input.txt'

def read_as_list(filepath):
    with open(filepath) as f:
        return f.readlines()

rawlist = read_as_list(listfile)

coords = [['forward',0],['up',0],['down',0]]

for n in rawlist:
    coord = n.split()
    for x in coords:
        if coord[0] == x[0]:
            x[1] = (int)(x[1]) + (int)(coord[1])

print(coords)

depth = coords[2][1] - coords[1][1]

answer = depth * coords[0][1]

print(answer)