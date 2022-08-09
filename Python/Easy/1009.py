
def bitwiseComplement(n):
    output = ""
    for i in bin(n)[2:]:
        if i == "0":
            output += "1"
        elif i == "1":
            output += "0"
    return int(output,2)

n = 5
complement = bitwiseComplement(n)
print(complement)
