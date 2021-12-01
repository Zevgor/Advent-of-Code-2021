listfile = 'Dec 1\Dec 1 input.txt'

def read_as_list(filepath):
    with open(filepath) as f:
        return [int(x) for x in f.readlines()]

rawlist = read_as_list(listfile)
inctally = 0

for idx,n in enumerate(rawlist):
    if idx+3 < len(rawlist):
        if rawlist[idx+3] > n:
            inctally+=1

print(inctally,"Increases")