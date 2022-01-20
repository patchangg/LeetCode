from collections import Counter

def rearrangeBarcodes(barcodes):
    i = 0
    n = len(barcodes)
    output = [0] * n
    codes = Counter(barcodes)
    for c,v in codes.most_common():
        for num in range(v):
            output[i] = c
            i += 2
            if i >= n:
                i = 1
    return output

# Sort the barcodes from most common to least. Put the numbers in the first,
# third, fifth, etc position until it reaches the end then put them in the
# second, fourth, sixth, etc position so no adjacent barcodes are equal.
# O(n + m) where n is the number of unique integers and m is the length
# of the barcodes, O(n) space
barcodes = [1,1,1,2,2,2]
rearrangedCodes = rearrangedBarcodes(barcodes)
print(rearrangedCodes)
