
def findTheWinner(n, k):
    list = [i for i in range(1,n+1)]
    curr = list[0]
    k = k - 1
    while len(list) != 1:
        index = list.index(curr)
        if index + k > len(list) - 1:
            index = ((index + k) % len(list))
            if index > len(list):
                index -= len(list)
        else:
            index += k
        if index + 1 > len(list) - 1:
            curr = list[0]
        else:
            curr = list[index+1]
        list.pop(index)
    return list[0]


n = 6
k = 5
winner = findTheWinner(n,k)
print(winner)
