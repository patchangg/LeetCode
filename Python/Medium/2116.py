
def canBeValid(s, locked):
    if len(s) % 2 == 1:
        return False
    flex = 0
    op = 0
    cl = 0
    for i in range(len(s) - 1, -1 , -1):
        if locked[i] == '0':
            flex += 1
        elif s[i] == '(':
            op += 1
        elif s[i] == ')':
            cl += 1
        if flex - op + cl < 0:
            return False
    flex = 0
    op = 0
    cl = 0
    for i in range(len(s)):
        if locked[i] == '0':
            flex += 1
        elif s[i] == '(':
            op += 1
        elif s[i] == ')':
            cl += 1
        if flex + op - cl < 0:
            return False
    return True

# Do a right to left and left to right scan of the string, checking for the
# number of flexible/non locked characters and locked brackets. If there is to
# many open bracked in the right to left scan and closed brackets in the
# left to right scan, it will be unbalanced and invalid. O(n), O(1) space 
s = "))()))"
locked = "010100"
valid = canBeValid(s,locked)
print(valid)
