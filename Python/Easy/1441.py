
def buildArray(target, n):
    output = []
    array = []
    for i in range(1,n+1):
        if i in target:
            array.append(i)
            output.append("Push")
        else:
            output.append("Push")
            output.append("Pop")
        if array == target:
            break
    return output

target = [1,3]
n = 3
operations = buildArray(target,n)
print(operations)
