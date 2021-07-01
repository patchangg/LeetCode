
def customSortString(order, string):
    arr = []
    for s in order:
        arr.append(s*string.count(s))
    for i in string:
        if i not in order:
            arr.append(i)
    return ''.join(arr)

# Append the characters that are in both order and the string then append the remaining
# characters in str. O(n + n) = O(n)
