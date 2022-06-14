
def minBitFlips(start, goal):
    binary = bin(start^goal)
    return binary.count("1")

start = 10
goal = 7
bitFlips = minBitFlips(start,goal)
print(bitFlips)
