
def minimumDeletions(s):
    flip = 0
    bCount = 0
    for i in s:
        if i == 'a':
            flip = min(bCount,flip+1)
        else:
            bCount += 1
    return flip

# Remove the a in the string or keep it depending on how many b's have been
# seen in the before the current index.
# O(n), O(1) space
s = "aababbab"
minDeletes = minimumDeletions(s)
print(minDeletes)
