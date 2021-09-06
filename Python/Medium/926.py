
def minFlipsMonoIncr(s):
    one = 0
    flip = 0
    for i in s:
        if i == '1':
            one += 1
        else:
            flip += 1
        flip = min(one,flip)
    return flip

# Loop through each character in the string
# For a monotone increasing array, we don't have to do anything if we get 1
# but if we get 0, we have to decide to flip the bit or flip all the ones
# that occured previously before the current index to maintain monotone array
# so we check the minimum of flipping the ones compared to flipping the zeroes
# to get a minimum flipped monotone array. O(n), O(1) space
s = "00110"
minFlips = minFlipsMonoIncr(s)
print(minFlips)
