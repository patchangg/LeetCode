import heapq

def kSmallestPairs(nums1, nums2, k):
    output = []
    if nums1 and nums2:
        queue = [(nums1[0] + nums2[0], (0,0))]
        visited = {}
        while len(output) < k and queue:
            value, (i, j) = heapq.heappop(queue)
            output.append((nums1[i],nums2[j]))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited[(i,j+1)] = 1
            if i + 1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(queue, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited[(i+1,j)] = 1
    return output

# BFS starting from the top left position of the nums1 * nums2 matrix,
# using a heap to store the values of the position. Go through the smallest
# values until k pairs are in the output. O(nlogn), O(n) space
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
smallestPairs = kSmallestPairs(nums1,nums2,k)
print(smallestPairs)
