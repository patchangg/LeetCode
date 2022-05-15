
def removeKdigits(num, k):
    string = list()
    for n in num:
        while string and k and string[-1] > n:
            string.pop()
            k -= 1

        if string or n != '0':
            string.append(n)

    if k:
        string = string[0:-k]

    if string:
        return "".join(string)
    else:
        return "0"

# Starting from the left, remove larger numbers found in the stack compared
# to the current number. If the number is a leading 0, don't put it into the stack.
# If k remains after going through the num string, remove the k digits from the
# right as they are larger than the numbers on the left side.
# If the string is empty at the end, return 0 otherwise join the new number
# from the stack back into a string. O(nlogn), O(n) space
num = "1432219"
k = 3
minNumber = removeKdigits(num,k)
print(minNumber)
