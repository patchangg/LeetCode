
def reformatNumber(number):
    output = []
    number = number.replace("-", "")
    number = number.replace(" ", "")
    n = len(number)
    i = 0
    while i < n:
        if i + 4 == n:
            output.append(number[i:i+2])
            i += 2
        elif i + 3 <= n:
            output.append(number[i:i+3])
            i += 3
        else:
            output.append(number[i:i+2])
            i += 2

    if len(output) > 1:
        return "-".join(output)
    return output[0]

number = "1-23-45 6"
reformatted = reformatNumber(number)
print(reformatted)
