
def maxDiff(num):
    a = str(num)
    b = str(num)

    for num in a:
        if num != "9":
            a = a.replace(num,"9")
            break

    if b[0] != "1":
        b = b.replace(b[0],"1")
    else:
        for digit in b[1:]:
            if digit not in "01":
                b = b.replace(digit,"0")
                break

    return int(a) - int(b)

# Transform the number into a string
# We want to find the maximum difference between two numbers
# Replace the first instance of a non 9 in the max number and replace
# the first instance of a non 0 or 1 in the min number to create a pair of
# min and max numbers. O(n), O(n) space
num = 555
maxDifference = maxDiff(num)
print(maxDifference)
