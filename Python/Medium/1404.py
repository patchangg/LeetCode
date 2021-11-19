
def numSteps(self, s: str) -> int:
    output = 0
    carry = 0
    for i in range(len(s)-1,0,-1):
        if int(s[i]) + carry == 1:
            carry = 1
            output += 2
        else:
            output += 1
    return output + carry

# Go right to left excluding the most right digit to check the number.
# If it ends in a 0, it's even and if it ends in a 1, its odd.
# Odd steps require 2 operations, add one and then divide by two.
# Even steps only need to divide by two.
# We need to carry the extra step, so when carry = 1 we need an additional
# operation to reduce the final step to 2. O(n), O(1) space
s = "1101"
binaryToOne = numSteps(s)
print(binaryToOne)
