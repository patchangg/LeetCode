
def bulbSwitch(n):
    return int(sqrt(n))

# A pattern appears where every i'th bulb only turns on during i^2 turn
# For for i bulb, you can get at most sqrt(i) bulbs on. O(1), O(1) space
n = 3
litBulbs = bulbSwitch(n)
print(litBulbs)
