
def maximumNumber(num, change):
    num = list(num)
    changed = False
    for i in range(len(num)):
        n = int(num[i])
        if change[n] > n:
            num[i] = str(change[n])
            changed = True
        elif changed and change[n] < n:
            break
    return "".join(num)

# Convert the num string to a list to go through it.
# Check each number left to right to see if the number it can be changed
# with is greater than it, if it is change it and turn the boolean flag on
# so to start the subarray from the index onwards. If a smaller number is in the
# change compared to the index number, break the loop and return the new
# maximum number. O(n), O(n) space
num = "132"
change = [9,8,5,0,3,6,4,2,6,8]
maximumNum = maximumNumber(num,change)
print(maximumNum)
