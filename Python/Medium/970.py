
def powerfulIntegers(x, y, bound):
    xSet = [x**i for i in range(20) if x**i <= bound]
    ySet = [y**j for j in range(20) if y**j <= bound]
    output = []

    for x in xSet:
        for y in ySet:
            if x + y <= bound:
                output.append(x+y)
    return set(output)

# Bruce force all the possible numbers created by x and y that is smaller
# than the bound. Check if the two numbers created added together is less
# than or equal to the bound number, if so add it to the set
# O(n^2), O(n) space
x = 2
y = 3
bound = 10
powerfulNumbers = powerfulIntegers(x,y,bound)
print(powerfulNumbers)
