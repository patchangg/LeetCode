from collections import OrderedDict

def kthDistinct(arr, k):
    counted = OrderedDict()
    for c in arr:
        if c in counted:
            counted[c] += 1
        else:
            counted[c] = 1

    for key, value in counted.items():
        if value == 1:
            k -= 1
            if k == 0:
                return key
    return ""

arr = ["d","b","c","b","c","a"]
k = 2
kDistinct = kthDistinct(arr,k)
print(kDistinct)
