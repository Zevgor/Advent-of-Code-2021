listfile = 'Dec 2\Dec 2 input.txt'

def read_as_list(filepath):
    with open(filepath) as f:
        return f.readlines()

rawlist = read_as_list(listfile)

pos = [0,0]
aim = 0

for n in rawlist:
    coord = n.split()
    if coord[0] == 'down':
        aim = aim + int(coord[1])
    elif coord[0] == 'up':
        aim = aim - int(coord[1])        
    elif coord[0] == 'forward':
        pos[0] = pos[0] + int(coord[1])
        pos[1] = pos[1] + (int(coord[1])*aim)

print(pos)

answer = pos[0] * pos[1]

print(answer)