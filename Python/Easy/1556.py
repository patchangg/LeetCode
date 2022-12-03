
def thousandSeparator(n):
    output = []
    n = str(n)
    count = 0
    for c in n[::-1]:
        if count == 3:
            output.append(".")
            count = 0
        count += 1
        output.append(c)
    return "".join(output)[::-1]

n = 987
dotSeperator = thousandSeparator(n)
print(dotSeperator)
