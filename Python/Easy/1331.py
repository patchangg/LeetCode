
def arrayRankTransform(arr):
    order = sorted(arr)
    rank = {}
    i = 1
    for num in order:
        if num not in rank:
            rank[num] = i
            i += 1
    for i in range(len(arr)):
        arr[i] = rank[arr[i]]
    return arr

arr = [40,10,20,30]
ranks = arrayRankTransform(arr)
print(ranks)
