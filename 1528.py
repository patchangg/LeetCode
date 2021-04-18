
def restoreString(s,indices):
    shuffled = ""
    for i in range(len(indices)):
        shuffled += s[indices.index(i)]
    return shuffled


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
s = restoreString(s,indices)
print(s)
