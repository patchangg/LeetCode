
def titleToNumber(columnTitle):
    output = 0
    for i, c in enumerate(reversed(columnTitle)):
        output += (26**i) * (ord(c) - ord('A') + 1)
    return output

columnTitle = "A"
excelSheetNumber = titleToNumber(columnTitle)
print(excelSheetNumber)
