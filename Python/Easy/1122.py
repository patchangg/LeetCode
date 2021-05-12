
def relativeSortArray(arr1, arr2):
    list1 = []
    list2 = []
    for num in arr1:
        if num in arr2:
            list1.append(num)
        else:
            list2.append(num)
    list2.sort()
    list1.sort(key=lambda x:arr2.index(x))
    return list1 + list2

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
relative = relativeSortArray(arr1,arr2)
print(relative)
