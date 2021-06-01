
def minFlips(target):
    output = 0
    previous = "0"
    for char in target:
        if char != previous:
            output += 1
            previous = char
    return output

target = "00000"
minimum = minFlips(target)
print(minimum)
