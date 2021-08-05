from itertools import combinations

def combine(n, k):
    array = [i for i in range(1,n+1)]
    output = combinations(array,k)
    return output

# Use the combinations function to get every combination from 1 to n, size k
# O(n! * n) where n = input size, O(n) space
n = 4
k = 2
combinations = combine(n,k)
print(combinations)
