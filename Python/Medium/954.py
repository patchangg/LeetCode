from collections import Counter

def canReorderDoubled(arr):
    counted = Counter(arr)
    for num in sorted(arr, key = abs):
        if counted[num] == 0:
            continue
        if counted[2*num] == 0:
            return False
        counted[num] -= 1
        counted[2*num] -= 1
    return True

# Count the numbers in the array. Go through the array sorted with the key being
# abs(num), so that we can check if there if there is another pair inside the array
# If there is remove one from the counter otherwise return False. O(nlogn), O(n)
# space
arr = [3,1,3,6]
doublePairs = canReorderDoubled(arr)
print(doublePairs)
