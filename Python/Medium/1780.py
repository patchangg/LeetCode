
powerofthree = [3 ** i for i in reversed(range(15))]
def checkPowersOfThree(n):
    for p in powerofthree:
        if n >= p:
            n -= p
    if n > 0:
        return False
    else:
        return True

# Maximum n can be is 10^7 so we only need to go 3^15 to match the highest power
# Keep removing the highest power of 3 in the array from n.
# if n > 0 that means that the number couldn't be only subtracted using powers
# of three so return false. O(n) where n is 15, O(1) space
n = 91
checked = checkPowersOfThree(n)
print(checked)
