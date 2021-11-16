
def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
    jumbo = (tomatoSlices - 2 * cheeseSlices) / 2
    small = (cheeseSlices - jumbo)
    if int(jumbo) == jumbo and int(small) == small and jumbo >= 0 and small >= 0:
        return [int(jumbo), int(small)]
    return []

# Math Question, O(1), O(1) space
# jumbo * 4 + small * 2 = tomatoSlices
# jumbo + small = cheeseSlices
# small = cheeseSlices - jumbo
# jumbo * 4 + (cheeseSlices - jumbo) * 2 = tomatoSlices
# jumbo * 4 cheeseSlices * 2 - jumbo * 2 = tomatoSlices
# jumbo = (tomatoSlices - cheeseSlices * 2) / 2
tomatoSlices = 16
cheeseSlices = 7
numNoWasteBurgers = numOfBurgers(tomatoSlices,cheeseSlices)
print(numNoWasteBurgers)
