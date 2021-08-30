
def rotatedDigits(n):
    output = 0
    skips = '347'
    valid = '2569'
    for i in range(1,n+1):
        number = str(i)
        if any(skip in number for skip in skips):
            continue
        if any(legit in number for legit in valid):
            print(number)
            output += 1
    return output

# 0, 1 and 8 are bad numbers as they rotate and become themselves which means
# they remain unchanged after flipping
# 2 flips to 5, 6 flips to 9 and vice versa so they are good integers as they
# are valid numbers after flipping
# This means that if the number contains 3, 4 or 7, that means it is automatically
# a bad number. So check if the num has 3, 4 or 7 then check if they contain only
# 2, 5, 6 and 9 digits in the number. O(n * 7) = O(n), O(1) space
n = 10
goodIntgers = rotatedDigits(n)
print(goodIntgers)
