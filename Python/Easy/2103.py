from collections import defaultdict

def countPoints(rings):
    hashmap = defaultdict(set)
    output = 0
    for i in range(0, len(rings)-1, 2):
        hashmap[rings[i+1]].add(rings[i])
    for s in hashmap.values():
        if len(s) == 3:
            output += 1
    return output

rings = "B0B6G0R6R0R6G9"
numPoints = countPoints(rings)
print(numPoints)
