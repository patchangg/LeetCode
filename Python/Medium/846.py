from collections import Counter

def isNStraightHand(hand, groupSize):
    counted = Counter(hand)
    for i in sorted(counted):
        if counted[i] > 0:
            for j in range(groupSize)[::-1]:
                counted[i+j] -= counted[i]
                if counted[i+j] < 0:
                    return False
    return True

# Count the numbers in the array
# Loop through the Counter and check if gS number ahead has the same amount or
# more count than the integer so that we can divide the array into sets of gS
# If it doesn't than that means we can't split the array so return False
# Do this for every number and return True.
# O(nlogn + n*gS), O(n) space
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
isStraightHand = isNStraightHand(hand,groupSize)
print(isStraightHand)
