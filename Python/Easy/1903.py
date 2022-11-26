
def largestOddNumber(num):

    for i in reversed(range(len(num))):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    return ""

num = "52"
biggestOddNumber = largestOddNumber(num)
print(biggestOddNumber)
