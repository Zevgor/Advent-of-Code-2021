listfile = 'Dec 1\Dec 1 input.txt'

def read_as_list(filepath):
    with open(filepath) as f:
        return [int(x) for x in f.readlines()]

rawlist = read_as_list(listfile)
inctally = 0

tuples = []

for idx,n in enumerate(rawlist):
    if len(rawlist)-idx > 2:
        tuples.append((rawlist[idx],rawlist[idx+1],rawlist[idx+2]))

inctally = 0
prevsum = sum(tuples[0])
tuples.pop(0)

for n in tuples:
    tuplesum = sum(n)
    if tuplesum > prevsum:
        inctally += 1
    prevsum = tuplesum

print(inctally,"Increases")