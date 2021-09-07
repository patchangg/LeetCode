
def lexicalOrder(self, n: int) -> List[int]:
    arr = [str(i) for i in range(1,n+1)]
    arr = sorted(arr)
    return arr

# Python sorted sorts alphabet letters in lexical order so create an array
# containing 1 to n integers but as strings and then sort them
# O(n), O(1) space
n = 13
lexical = lexicalOrder(n)
print(lexical)
