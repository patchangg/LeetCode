
def reverse(x):
    sign = 1
    if x < 0:
        sign = -1
    output = sign * int(str(abs(x))[::-1])
    if -2**31 <= output <= (2**31 - 1):
        return output
    else:
        return 0

# Check for the sign at the front, convert the number into a string and reverse it
# Change the reversed string back into a integer and return it if its between
# -2^31 and 2^31 -1. O(1), O(n) space
x = 123
reversedX = reverse(x)
print(reversedX)
