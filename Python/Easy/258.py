
def addDigits(num):
    while len(str(num)) > 1:
        digits = str(num)
        total = 0
        for c in digits:
            total += int(c)
        num = total
    return num

num = 38
oneDigitNum = addDigits(num)
print(oneDigitNum)
