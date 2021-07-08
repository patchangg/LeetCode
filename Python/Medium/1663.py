
def getSmallestString(n, k):
    output = [1] * n
    k -= n
    cur = -1
    while k:
        index = min(25,k)
        k -= index
        output[cur] += index
        cur -= 1
    return ''.join(chr(ord('a')+c-1) for c in output)

# Create a array filled with 1's/a's and remove n from k
# This means we have all the slots filled with a padding while k > 25
# Use greedy to put z's into the string until it is less than 25
# then place the final string as k
# then convert the numbers into lower case alphabet letters.
# O(n) as we need to get n amount of characters, O(n) space for the array
n = 5
k = 73
smallest = getSmallestString(n,k)
print(smallest)
