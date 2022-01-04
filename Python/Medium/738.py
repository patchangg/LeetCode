
def monotoneIncreasingDigits(n):
    if n < 10:
        return n
    output = list(str(n))
    i = 0
    l = len(output)
    while i < l-1 and output[i] <= output[i+1]:
        i += 1

    if i == l-1:
        return n

    while i > 0 and output[i] == output[i-1]:
        i -= 1

    output[i] = str(int(output[i]) - 1)
    output[i+1:] = ['9'] * (l-i-1)
    return int(''.join(output))

# Find where the integer starts to decrease digit wise. This is where we will
# start to decrease the number by 1 and replace to the rest with 9's to
# get monotone increasing digits. If the number is equal to the previous digit
# keep going down until you reach it so its a higher integer in the end.
# O(n), O(n) space
n = 10
largestNumber = monotoneIncreasingDigits(n)
print(largestNumber)
