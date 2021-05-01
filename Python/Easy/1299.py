
def replaceElements(arr):
    length = len(arr)
    i = 0
    output = []
    if length == 1:
        output.append(-1)
        return output
    while i < length - 1:
        output.append(max(arr[i+1:]))
        i += 1
    output.append(-1)
    return output
    #     max = 0
    #     for s in range(i+1,length):
    #         if arr[s] > max:
    #             max = arr[s]
    #         s += 1
    #     output.append(max)
    #     i += 1
    # output.append(-1)
    # return output

arr = [17,18,5,4,6,1]
replaced = replaceElements(arr)
print(replaced)
