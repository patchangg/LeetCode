
def closetTarget(words, target, startIndex):
    l = -1
    r = -1
    n = len(words)
    for i in range(len(words)):
        if words[(startIndex+i) % n] == target:
            l = i
            break
    for j in range(len(words)):
        if words[(startIndex-j) % n] == target:
            r = j
            break
    return min(l,r)

words = ["hello","i","am","leetcode","hello"]
target = "hello"
startIndex = 1
shortestDistance = closetTarget(words,target,startIndex)
print(shortestDistance)
