
def findComplement(num):
    output = ""
    for i in bin(num)[2:]:
        if i == "0":
            output += "1"
        elif i == "1":
            output += "0"
    return int(output,2)

num = 5
complement = findComplement(num)
print(complement)
