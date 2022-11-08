from itertools import permutations

def findEvenNumbers(digits):
    output = set()
    for x, y, z in permutations(digits, 3):
        if x != 0 and z % 2 == 0:
            output.add(x*100+y*10+z)
    return sorted(output)

digits = [2,1,3,0]
evenPermutations = findEvenNumbers(digits)
print(evenPermutations)
