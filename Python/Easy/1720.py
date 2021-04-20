
def decode(encoded, first):
    encoded.insert(0,first)
    for i in range(1,len(encoded)):
        encoded[i] ^= encoded[i-1]
    return encoded

encoded = [6,2,7,3]
first = 4
arr = decode(encoded,first)
print(arr)
