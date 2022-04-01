
def hIndex(citations):
    citations = sorted(citations)
    length = len(citations)
    for i in range(length):
        if citations[i] >= length - i:
            return length - i
    return 0

# Sort the citations. Go through the citations, find the index where the
# citation value is value = length minus index which means that number of citations
# is value or greater. O(nlogn), O(1) space
citations = [3,0,6,1,5]
index = hIndex(citations)
print(index)
