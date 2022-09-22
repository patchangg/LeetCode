
def binaryGap(n):
    b = str(bin(n)[2:])
    n = -1
    output = 0
    for i in range(len(b)):
        if b[i] == "1" and n == -1:
            n = i
        elif b[i] == "1":
            output = max(output, i - n)
            n = i
    return output

n = 22
gapLength = binaryGap(n)
print(gapLength)
