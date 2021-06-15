from itertools import permutations

def numTilePossibilities(tiles):
    length = len(tiles)
    charList = [char for char in tiles]
    perms = []
    for i in range(1,length+1):
        perms += permutations(charList,i)
        print(perms)
    perms = set(perms)
    return len(perms)

tiles = "AAB"
number = numTilePossibilities(tiles)
print(number)
