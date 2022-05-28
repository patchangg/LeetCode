
def myAtoi(s):
    arr = list(s.strip())
    if len(arr) == 0:
        return 0
    sign = 1
    if arr[0] == '-':
        sign = -1
    output = 0
    i = 0
    if arr[0] in ['-','+']:
        i += 1
    while i < len(arr) and arr[i].isdigit():
        output = output * 10 + ord(arr[i]) - ord('0')
        i += 1
    return max(-2**31, min(output*sign, 2**31 - 1))

# Remove any leading whitespaces and split the string into a list
# Check for the sign at the front and skip that index.
# Go through the list from the start until the end or characters start showing
# up, converting the string into a number. O(n), O(n) space
s = "42"
atoi = myAtoi(s)
print(atoi)
