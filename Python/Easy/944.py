
def minDeletionSize(strs):
    deleted = 0
    length = len(strs)
    lenStr = len(strs[0])
    for i in range(lenStr):
        if lenStr == 1:
            word = strs[i]
        else:
            word = strs[0][i]
        for s in range(length):
            if lenStr != 1:
                if strs[s][i] < word:
                    deleted += 1
                    break
                else:
                    word = strs[s][i]
            else:
                if strs[s] < word:
                    deleted += 1
                    break
                else:
                    word = strs[i]
    return deleted


#strs = ["a","b"]
strs = ["rrjk","furt","guzm"]
deleted = minDeletionSize(strs)
print(deleted)
