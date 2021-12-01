listfile = 'Dec 1\Dec 1 input.txt'

def read_as_list(filepath):
    with open(filepath) as f:
        return [int(x) for x in f.readlines()]

rawlist = read_as_list(listfile)
prevnum = rawlist.pop(0)
inctally = 0

for n in rawlist:
    #if new number > previous number, increment inctally
    if n > prevnum:
        inctally+=1
    prevnum = n

print(inctally,"Increases")