
def numberOfWeakCharacters(properties):
    output = 0
    curr = 0
    properties = sorted(properties,key=lambda x: (-x[0],x[1]))
    for i, c in properties:
        if c < curr:
            output += 1
        else:
            curr = c
    return output

# Sort the attack descending and defense ascending to get the weakest characters.
# O(nlogn), O(n) space
properties = [[5,5],[6,3],[3,6]]
weakChars = numberOfWeakCharacters(properties)
print(weakChars)
