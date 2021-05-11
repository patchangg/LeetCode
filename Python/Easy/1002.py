
def commonChars(A):
    common = list(A[0])
    for word in A[1:]:
        check = []
        for char in word:
            if char in common:
                check.append(char)
                common.remove(char)
        common = check
    return common

A = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
common = commonChars(A)
print(common)
