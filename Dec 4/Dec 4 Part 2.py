import sys

listfile = 'Dec 4\Dec 4 input.txt'

def remove_items(list,item):
    res = [i for i in list if i != item]
    return res

def print_winner(bingocard,drawnum):
    answer = 0
    print("last number:", drawnum)
    for row in bingocard:
        print(row[0],row[1],row[2],row[3],row[4])
        row = remove_items(row,'X')
        print(row)
        for num in row:
            answer = answer + int(num)
    answer = answer * int(drawnum)
    print ("answer",answer)

lines = []
with open(listfile) as f:
    lines = f.readlines()

# count = 0
# for line in lines:
#     count += 1
#     print(f'line {count}: {line}')

#process 1st line into it's own list
draworder = lines[0].split(',')
del lines[0]

#cleanup blank lines
lines = remove_items(lines,"\n")

cardlist = []
cardrows = []

cardrowcount = 0
#load cards
for line in lines:
    #remove newline
    line = line.strip()
    
    #add row to rowlist
    numlist = line.split(' ')
    numlist = remove_items(numlist,'')
    cardrows.append(numlist)

    #iterate counter
    cardrowcount += 1

        #if 5th row (4), reset to 1 for new card
    if cardrowcount > 4:
        cardrowcount = 0
        cardlist.append(cardrows.copy())
        cardrows.clear()

#at this point we have a 2d array, cardlist, arranges as such:

#[XX XX XX XX XX
# XX XX XX XX XX
# XX XX XX XX XX
# XX XX XX XX XX
# XX XX XX XX XX] x 100

for idxdn,drawnum in enumerate(draworder):
    #print('checking',drawnum)
    for idxbc,bingocard in enumerate(cardlist):
        #print('is it in here?',bingocard,idxbc)
        for idxcr,cardrow in enumerate(bingocard):
            for idxrn,rownum in enumerate(cardrow):
                #print('row',idxcr,'num',rownum)
                if rownum == drawnum:
                    #print('hit!',rownum,'=',drawnum,'on card',idxbc,'row',idxcr,'num',idxrn)
                    cardlist[idxbc][idxcr][idxrn] = 'X'
    #check for any completed cards
    for hitcard in cardlist:
        #print_card(hitcard)
        winner = 1
        for hitrow in hitcard:            
            winner = 1
            for hitnum in hitrow:
                if hitnum != 'X':
                    winner = 0
            if winner == 1:
                print("HORIZONTAL WINNER!")
                if len(cardlist) == 1:
                    print_winner(hitcard,drawnum)
                    sys.exit()
                cardlist = remove_items(cardlist,hitcard)
                print("Removed!")
        print("post break")
        winner = 1
        for n in range(0,5):
            #print (hitcard[0][n],hitcard[1][n],hitcard[2][n],hitcard[3][n],hitcard[4][n])
            winner = 1
            if hitcard[0][n] != 'X':
                winner = 0
            if hitcard[1][n] != 'X':
                winner = 0
            if hitcard[2][n] != 'X':
                winner = 0
            if hitcard[3][n] != 'X':
                winner = 0
            if hitcard[4][n] != 'X':
                winner = 0
            if winner == 1:
                break
        if winner == 1:#
            print("VERTICAL WINNER!")
            if len(cardlist) == 1:
                print_winner(hitcard,drawnum)
                sys.exit()
            cardlist = remove_items(cardlist,hitcard)