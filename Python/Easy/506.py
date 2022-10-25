
def findRelativeRanks(score):
    ranks = {}
    output = []
    pos = sorted(score)[::-1]
    for i in range(len(score)):
        if i == 0:
            ranks[pos[i]] = "Gold Medal"
        elif i == 1:
            ranks[pos[i]] = "Silver Medal"
        elif i == 2:
            ranks[pos[i]] = "Bronze Medal"
        else:
            ranks[pos[i]] = str(i + 1)
    for s in score:
        output.append(ranks[s])
    return output

score = [5,4,3,2,1]
rankings = findRelativeRanks(score)
print(rankings)
