listfile = 'Dec 3\Dec 3 input.txt'

def read_as_list(filepath):
    with open(filepath) as f:
        return f.readlines()

def parse(word):
    return [char for char in word]

def bintodec(n):
    return int(n,2)

def cleanup(inputlist,pos,bit):
    for x in reversed(range(len(inputlist))):
        if(int(inputlist[x][pos]) != int(bit)):
            inputlist.pop(x)
    return inputlist

def cleanupinv(inputlist2,pos2,bit2):
    for x in reversed(range(len(inputlist2))):
        if(int(inputlist2[x][pos2]) == int(bit2)):            
            inputlist2.pop(x)
    return inputlist2

rawlist = read_as_list(listfile)
parselist = []

for x in rawlist:
    parselist.append((parse((x).strip())))

#now do oxg
oxg = [0,0,0,0,0,0,0,0,0,0,0,0]
oxglist = parselist.copy()
co2list = parselist.copy()

parseavg = [0,0,0,0,0,0,0,0,0,0,0,0]
for idx,x in enumerate(oxg):
    #sum bites
    for j in oxglist:
        for idx3,n in enumerate(j):
            parseavg[idx3] += int(n)
    #get avg of bites
    for idx2,j2 in enumerate(parseavg):
        parseavg[idx2] = parseavg[idx2]/len(oxglist)
        if parseavg[idx2] < .5:
            parseavg[idx2] = 0
        elif parseavg[idx2] >= .5:
            parseavg[idx2] = 1
    #we have the avg # of bits represented as the binary in parseavg.
    #we need to select the next position (using oxg's IDX) and remove all items from oxglist that do not match the average bit in that position.
    #so CLEANUP from oxglist anything at IDX with value of PARSEAVG at IDX
    oxglist = cleanup(oxglist,idx,parseavg[idx])
    parseavg = [0,0,0,0,0,0,0,0,0,0,0,0]
    if len(oxglist) == 1:
        break

str_ints = (str(int) for int in oxglist[0])
gamma = ''.join(str_ints)
print(bintodec(gamma))

#now do co2
co2 = [0,0,0,0,0,0,0,0,0,0,0,0]

parseavg = [0,0,0,0,0,0,0,0,0,0,0,0]
for idx,x in enumerate(co2):
    #sum bites
    for j in co2list:
        for idx3,n in enumerate(j):
            parseavg[idx3] += int(n)
    #get avg of bites
    for idx2,j2 in enumerate(parseavg):
        parseavg[idx2] = parseavg[idx2]/len(co2list)
        if parseavg[idx2] < .5:
            parseavg[idx2] = 0
        elif parseavg[idx2] >= .5:
            parseavg[idx2] = 1
    #we have the avg # of bits represented as the binary in parseavg.
    #we need to select the next position (using co2's IDX) and remove all items from co2list that do not match the average bit in that position.
    #so CLEANUP from co2list anything at IDX with value of PARSEAVG at IDX
    co2list = cleanupinv(co2list,idx,parseavg[idx])
    parseavg = [0,0,0,0,0,0,0,0,0,0,0,0]
    if len(co2list) == 1:
        break

str_ints = (str(int) for int in co2list[0])
beta = ''.join(str_ints)
print(bintodec(beta))

print('Answer:',bintodec(gamma)*bintodec(beta))