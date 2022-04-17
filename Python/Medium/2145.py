
def numberOfArrays(differences, lower, upper):
    lo = lower
    up = upper
    for diff in differences:
        lo = max(lower,lo + diff)
        up = min(upper,up + diff)
        if lo > upper or up < lower:
            return 0
    return up - lo + 1

# Find the new min and max sequence between the numbers in differences to
# get the number of hidden sequences in the end. O(n), O(1) space
differences = [1,-3,4]
lower = 1
upper = 6
sequences = numberOfArrays(differences,lower,upper)
print(sequences)
