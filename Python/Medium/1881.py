
def maxValue(n, x):
    if n[0] == '-':
        i = 1
        while i < len(n) and x >= int(n[i]):
            i += 1
    else:
        i = 0
        while i < len(n) and x <= int(n[i]):
            i += 1
    return n[:i] + str(x) + n[i:]

# Loop through the string and check if the current number is greater than
# the x value. From that index, put x in the middle.
# Do the same for negative numbers but look if the current number is smaller
# than x. O(n), O(n) space
n = "99"
x = 9
maxValueAfterInsertion = maxValue(n,x)
