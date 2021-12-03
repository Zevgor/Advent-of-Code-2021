listfile = 'Dec 3\Dec 3 input.txt'

def read_as_list(filepath):
    with open(filepath) as f:
        return f.readlines()

def parse(word):
    return [char for char in word]

def bintodec(n):
    return int(n,2)

rawlist = read_as_list(listfile)
parselist = []

for x in rawlist:
    parselist.append((parse((x).strip())))

parseavg = [0,0,0,0,0,0,0,0,0,0,0,0]

for x in parselist:
    for idx,n in enumerate(x):
        parseavg[idx] += int(n)

for idx,x in enumerate(parseavg):
    parseavg[idx] = parseavg[idx]/len(parselist)
    if parseavg[idx] < .5:
        parseavg[idx] = 0
    elif parseavg[idx] > .5:
        parseavg[idx] = 1

str_ints = (str(int) for int in parseavg)
gamma = ''.join(str_ints)
print(bintodec(gamma))

for idx,x in enumerate(parseavg):
    if parseavg[idx] < .5:
        parseavg[idx] = 1
    elif parseavg[idx] > .5:
        parseavg[idx] = 0

str_ints2 = (str(int) for int in parseavg)
epsilon = ''.join(str_ints2)
print(bintodec(epsilon))

print('Answer:',bintodec(gamma)*bintodec(epsilon))