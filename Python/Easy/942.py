
def diStringMatch(s):
    array = [i for i in range(len(s)+1)]
    output = []
    for word in s:
        if word == "I":
            output.append(array.pop(0))
        elif word == "D":
            output.append(array.pop(-1))
    if array:
        output = output + array
    return output

s = "IDID"
perm = diStringMatch(s)
print(perm)
