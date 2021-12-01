
def minNumberOfFrogs(croakOfFrog):
    count = [0,0,0,0,0]
    croak = "croak"
    output = 0
    frogs = 0
    for char in croakOfFrogs:
        idx = croak.index(char)
        count[idx] += 1
        if idx == 0:
            frogs += 1
            output = max(output,frogs)
        elif count[idx-1] < count[idx]:
            return -1
        elif idx == 4:
            frogs -= 1
    if frogs == 0:
        return output
    else:
        return -1

# Count each letter of the string. If c appears, that means there is a new frog
# and if k appears that means a frog is gone. While checking for letters,
# if a letter in croak is higher than the letter after it, that means the
# combination is invalid. Also if a frog hasn't finished croaking, that means
# the combination is invalid. O(n), O(5) space
croakOfFrogs = "croakcroak"
numOfFrogs = minNumberOfFrogs(croakOfFrogs)
print(numOfFrogs)
