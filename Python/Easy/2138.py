
def divideString(s, k, fill):
    filled = s + (fill*(k-1))
    output = []
    for i in range(0, len(s), k):
        output.append(filled[i:i+k])
    return output

s = "abcdefghi"
k = 3
fill = "x"
dividedString = divideString(s,k,fill)
