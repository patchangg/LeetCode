
def fillCups(amount):
    output = 0
    amount = sorted(amount)

    while amount[2] > 0 and amount[1] > 0:
        amount[2] -= 1
        amount[1] -= 1
        output += 1
        amount = sorted(amount)

    while amount[2] > 0:
        amount[2] -= 1
        output += 1

    return output

amount = [1,4,2]
minTimeToFill = fillCups(amount)
print(minTimeToFill)
