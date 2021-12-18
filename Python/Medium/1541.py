
def minInsertions(s):
    s = s.replace("))","]")
    lCount = 0
    rCount = 0
    for c in s:
        if c == "(":
            lCount += 1
        elif (c == ")" or c == "]") and lCount > 0:
            lCount -= 1
            if c == ")":
                rCount += 1
        else:
            if c == ")":
                rCount += 2
            else:
                rCount += 1
    return rCount + (lCount * 2)

# Replace all instances of )) pairs to ] to make it easier to find the min number
# of insertions. Loop through the string, lCounting every ( as that must be paired
# with )). If any leftover ( in the string that doesn't have a pair, we multiply
# it by two as we need to insert those parentheses to balance it.
# If ) or ] is found and there are ( without any pairs, remove one from the (
# lCount as it is balanced, if it is a stray ), we need another ) to make it balanced
# If there is no ( counted or all are in a balanced pair, add two insertions for
# ) and one for ] to make it balanced. O(2n) = O(n), O(1) space
s = "(()))"
numInsertions = minInsertions(s)
print(numInsertions)
