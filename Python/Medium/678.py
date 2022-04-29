
def checkValidString(s):
    left = 0
    right = 0
    for c in s:
        if c == "(":
            left += 1
            right += 1
        if c == ")":
            right -= 1
            left = max(left - 1, 0)
        if c == "*":
            right += 1
            left = max(left - 1, 0)
        if right < 0:
            return False
    return left == 0

# Count the number of left, right parenthesis and *. There cannot ever be less
# than 0 ) and the ( has to be equal to 0 at the end for the string to be valid.
# If * is found, it can either lead to needing another ) being a ( subsitute
# or filling a ). O(n), O(1) space
s = "()"
validString = checkValidString(s)
print(validString)
