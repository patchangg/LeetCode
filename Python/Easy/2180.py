
def countEven(num):
    output = 0
    for i in range(2, num + 1):
        n = map(int, str(i))
        if sum(n) % 2 == 0:
            output += 1
    return output

num = 4
numEvenDigitSums = countEven(num)
print(numEvenDigitSums)
