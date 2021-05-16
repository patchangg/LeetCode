
def findTheDistanceValue(arr1, arr2, d):
    elements = 0
    for num in arr1:
        distance = True
        for n in arr2:
            if abs(num-n) <= d:
                distance = False
        if distance:
            elements += 1
    return elements

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
distance = findTheDistanceValue(arr1,arr2,d)
print(distance)
