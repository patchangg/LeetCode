
def countConsistentStrings(allowed, words):
    count = 0
    check = list(allowed)
    print(check)
    for word in words:
        counter = 0
        for char in word:
            if char not in check:
                counter += 1
        if counter == 0:
            count += 1
    return count

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
consistent = countConsistentStrings(allowed,words)
print(consistent)
