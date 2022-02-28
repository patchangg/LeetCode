
def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    zigzag = [''] * numRows
    index = 0
    step = 1
    for c in s:
        zigzag[index] += c
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step
    return ''.join(zigzag)

# Zigzag pattern with numRows 3 goes 0 1 2 1 0 1 2 ...
# So create an array sized numRows and create a counter that keeps track of
# where in the zigzag it is at and place each character in the string at
# the zigzag index it is in. Once the index reaches numRows, reverse it so
# it goes back to 0. O(n), O(numRows) space
s = "PAYPALISHIRING"
numRows = 3
zigzaged = convert(s,numRows)
print(zigzaged)
