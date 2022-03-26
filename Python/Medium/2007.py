from collections import Counter

def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []
    original = Counter(changed)
    output = []
    for num in sorted(changed):
        if num == 0 and original[0] > 1:
            original[num] -= 2
            output.append(num)
        elif num == 0 and original[0] <= 1:
            original[num] -= 1
            continue
        else:
            if original[num*2] > 0 and original[num] > 0:
                original[num] -= 1
                original[num*2] -= 1
                output.append(num)
    if len(output) == len(changed) // 2:
        return output
    else:
        return []

# Count the numbers in the changed array. If its not even, it is impossible
# to get the original array. 0 is a edge case as 0*2 = 0 so if there is multiple
# 0s, add one to the original array and remove two from the counter.
# If there is a double of a number in the changed array, remove the double
# and original from the counter. If the ending array is not half of the length
# of the changed array, it means it is impossible to get the original.
# O(nlogn), O(n) space 
changed = [1,3,4,2,6,8]
originalArray = findOriginalArray(changed)
print(originalArray)
