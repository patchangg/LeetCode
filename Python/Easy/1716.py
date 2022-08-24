
def totalMoney(n):
    output = 0
    week = 0
    for i in range(n):
        if i % 7 == 0:
            week += 1
        output += week + (i % 7)
    return output

n = 4
totalM = totalMoney(n)
print(totalM)
