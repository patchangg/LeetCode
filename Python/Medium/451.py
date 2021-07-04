
def frequencySort(self, s: str) -> str:
    dicts = {}
    output = []
    for c in s:
        if c in dicts:
            dicts[c] += 1
        else:
            dicts[c] = 1
    for k, v in sorted(dicts.items(), key = lambda x: -x[1]):
        output += [k] * v
    return "".join(output)

# Count the characters in the string into a hashmap
# Sort the dict based on the value and reverse it to get most frequent first
# Join the keys and return it. O(2*n) = O(n)
s = "tree"
frequency = frequencySort(s)
print(frequency)
