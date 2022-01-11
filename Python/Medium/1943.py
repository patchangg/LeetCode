from collections import defaultdict

def splitPainting(segments):
    mapping = defaultdict(int)
    for start,end,colour in segments:
        mapping[start] += colour
        mapping[end] -= colour

    prev = None
    colour = 0
    output = []
    for segment in sorted(mapping):
        if prev != None and colour > 0:
            output.append((prev,segment,colour))
        colour += mapping[segment]
        prev = segment
    return output

# For each segment, where it starts add the colour and where it ends subtract
# the colour. Sort the mapping of start and end points and count the cost between
# each non overlapping segment in the mapping and append its range and unique
# colour integer into an array. O(nlogn), O(n) space
segments = [[1,4,5],[4,7,7],[1,7,9]]
uniqueSegments = splitPainting(segments)
print(uniqueSegments)
