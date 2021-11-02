
def numPairsDivisibleBy60(self, time: List[int]) -> int:
    arr = [0] * 60
    output = 0
    for t in time:
        output += arr[-t % 60]
        arr[t % 60] += 1
    return output

# Create array size 60. For each time store its modulo 60 into the array and
# add the amount of pairs it can get into the result as if there is another number
# that has been seen that equals (seen + num) % 60 == 0, we can create that many
# pairs. O(n), O(1) space
time = [30,20,150,100,40]
numPairs = numPairsDivisibleBy60(time)
print(numPairs)
