
def uniqueOccurrences(arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i] += 1
        elif i not in dic:
            dic[i] = 1
    arr = []
    for value in dic.values():
        if value in arr:
            return False
        arr.append(value)
    return True

arr = [1,2,2,1,1,3]
isUnique = uniqueOccurrences(arr)
print(isUnique)
