
def modifyString(s):
    output = list(s)
    for i, c in enumerate(s):
        if c != "?":
            output[i] = c
        else:
            for ch in "abc":
                if (i+1 == len(s) or output[i+1] != ch) and (i == 0 or output[i-1] != ch):
                    output[i] = ch
                    break
    return "".join(output)

s = "?zs"
removeQuestionMarks = modifyString(s)
print(removeQuestionMarks)
