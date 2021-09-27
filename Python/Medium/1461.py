
def hasAllCodes(self, s: str, k: int) -> bool:
    seen = set()
    queue = deque()
    for char in s:
        queue.append(char)
        if len(queue) == k:
            seen.add(''.join(queue))
            queue.popleft()
    return len(seen) == 1 << k

# Sliding window problem
# Create a sliding window k size in s and append the substring into a set
# Check if the length of the set is the same as every possible binary
# combination of k length which is 1 << k number
# O(n), O(n) space
s = "00110110"
k = 2
everyBinaryCode = hasAllCodes(s,k)
print(everyBinaryCode)
