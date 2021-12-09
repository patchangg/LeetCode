
def lenLongestFibSubseq(self, arr: List[int]) -> int:
    s = set(arr)
    output = 2
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            a, b, l = arr[i],arr[j],2
            while a + b in s:
                a, b, l = b, a + b, l+1
            output = max(output,l)
    if output > 2:
        return output
    else:
        return 0

# The subsequence must be at least 3 integers long. For every number combination
# in the array, check if the next fib sequence after adding the two numbers
# exist in the array until the next sequence is not found, recording the length
# of the subsequence. Return the longest fib subsequence found in the array.
# O(n^2 * log(m)) where m is the time to get to the number m. O(n) space
arr = [1,2,3,4,5,6,7,8]
longestFibSubsequence = lenLongestFibSubseq(arr)
print(longestFibSubsequence)
