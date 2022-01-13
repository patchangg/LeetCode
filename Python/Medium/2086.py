
def minimumBuckets(street):
    if "HHH" in street:
        return -1
    if street[:2] == "HH":
        return -1
    if street[-2:] == "HH":
        return -1
    if street == "H":
        return -1
    return street.count("H") - street.count("H.H")

# Check all the cases that would make collecting rainwater impossible
# Cound all the Homes and minus and homes that have space between them
# O(n), O(1) space
street = "H..H"
numBuckets = minimumBuckets(street)
print(numBuckets)
