
def numberOfLines(widths, s):
    output = [1,0]
    line = 0
    for c in s:
        width = widths[ord(c) - ord('a')]
        if line + width > 100:
            output[0] += 1
            line = width
        else:
            line += width
    output[1] = line
    return output

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
numLines = numberOfLines(widths,s)
print(numLines)
