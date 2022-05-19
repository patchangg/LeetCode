from collections import defaultdict

def countPairs(deliciousness):
    pairs = defaultdict(int)
    output = 0
    for food in deliciousness:
        for i in range(22):
            output += pairs[2**i - food]
        pairs[food] += 1
    return output % (10**9 + 7)

# For each power of 2 up to 22, find if any pairs exist in the dictionary
# that counts each occurence of every number in the array. O(22n) = O(n),
# O(n) space
deliciousness = [1,3,5,7,9]
pairsOfFood = countPairs(deliciousness)
print(pairsOfFood)
