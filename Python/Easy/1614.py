
def maxDepth(s):
    maximum = 0
    counter = 0
    for char in s:
        if char == "(":
            counter += 1
            if counter > maximum:
                maximum = counter
        elif char == ")":
            counter -= 1
    return maximum

s = "(1+(2*3)+((8)/4))+1"
max = maxDepth(s)
print(max)
