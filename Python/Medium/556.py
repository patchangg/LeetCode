
def nextGreaterElement(self, n: int) -> int:
    if n < 10:
        return -1

    n = list(str(n))
    index = -1
    r = -1
    output = -1

    for i in range(len(n)-1,0,-1):
        if n[i] > n[i-1]:
            index = i - 1
            break

    for i in range(len(n)-1,0,-1):
        if n[i] > n[index]:
            r = i
            n[index],n[r] = n[r],n[index]
            n = "".join(n)
            break

    if index != -1:
        temp = n[index+1:]
        s = n[:index] + n[index] + temp[::-1]
        output =  int(s)

    if output < 2**31:
        return output
    else:
        return -1

# Find the first digit that is smaller than the previous from right to left
# Find the next greater digit from right to left bigger than the previous
# number found, swap them and record the index positions. Reverse the numbers
# to the right of the first index found to get the next greatest number.
# O(n), O(n) space
n = 12
greaterElement = nextGreaterElement(n)
print(greaterElement)
