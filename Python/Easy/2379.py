
def minimumRecolors(blocks, k):
    white = 0
    for i in range(k):
        if blocks[i] == "W":
            white += 1
    output = white
    for r in range(k,len(blocks)):
        if blocks[r] == "W":
            white += 1
        if blocks[r-k] == "W":
            white -= 1
        output = min(output,white)
    return output

blocks = "WBBWWBBWBW"
k = 7
minOperations = minimumRecolors(blocks,k)
print(minOperations)
