from collections import Counter

def bestHand(ranks, suits):
    if len(set(suits)) == 1:
        return "Flush"
    counted = Counter(ranks)
    value = counted.most_common(1)[0][1]
    if value >= 3:
        return "Three of a Kind"
    elif value == 2:
        return "Pair"
    else:
        return "High Card"

ranks = [13,2,3,1,9]
suits = ["a","a","a","a","a"]
bestPlay = bestHand(ranks,suits)
print(bestPlay)
