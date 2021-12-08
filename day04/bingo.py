# Bingo


class bingocard:
    def __init__(self, name, strings_in):
        self.name = name;
        self.card = list()
        self.bingo = 0

        for line in strings_in:
            self.card.append(list(line));


    def __str__(self):
        return f"Bingo card {self.name} is bingo state {self.bingo}\n{self.card[0]}\n{self.card[1]}\n{self.card[2]}\n{self.card[3]}\n{self.card[4]}\n";

    def isbingo(self):
        return self.bingo

    def pick(self, pick):
        for row,line in enumerate(self.card):
            for col,spot in enumerate(line):
                if spot == pick:
                    self.card[row][col] = str("x" + pick)
            
            # check if this line is bingo
            if ''.join(line).count('x') == 5:
                self.bingo = 1
                return 1

        # check columns for bingo
        col = 0
        while col < 5:
            column = list()
            for line in self.card:
                column.append(line[col])

#            print(column)
            if ''.join(column).count('x') == 5:
                self.bingo = 1
                return 1
            
            del column
            col += 1

    def prune_xs(self):
        self.pruned = list()
        for line in self.card:
            for spot in line:
                if spot.count('x') == 0:
                    self.pruned.append(spot)
        
        print(self.pruned)
        self.prunesum = 0
        for spot in self.pruned:
            self.prunesum += int(spot)

        return self.prunesum

# function to prune list based on most common bit
def prune_list(list_in, place, value):
  list_in[:] = (state for state in list_in if int(state[place]) == value)

# Start
cards = list()

with open('input.txt', 'r') as inputfile:
    # first line are the picks
    picks = list(inputfile.readline().strip().split(","))
    print(picks)

    cardno = 0

    # blank line
    while inputfile.readline():
        # read card
        tempcard = list()
        tempcard.append(list(inputfile.readline().strip().split()))
        tempcard.append(list(inputfile.readline().strip().split()))
        tempcard.append(list(inputfile.readline().strip().split()))
        tempcard.append(list(inputfile.readline().strip().split()))
        tempcard.append(list(inputfile.readline().strip().split()))

        cards.append(bingocard(str(cardno), tempcard))
        del tempcard
        cardno += 1


winners = 0
for newpick in picks:
    for currcard in cards:
        if currcard.isbingo() == 0:
            isbingo = currcard.pick(newpick)
            if isbingo == 1:
                if winners == 0:
                    print(f"first winner, pick: {newpick}")
                    print(currcard)
                    print(int(currcard.prune_xs()) * int(newpick))
                winners += 1
    
                if winners == len(cards):
                    print(f"last winner, pick: {newpick}")
                    print(currcard)
                    print(int(currcard.prune_xs()) * int(newpick))
                    quit()
