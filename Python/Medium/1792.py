import heapq

def maxAverageRatio(classes, extraStudents):
    heap = [(((p/t)-(p+1)/(t+1)),p,t) for p,t in classes]
    heapify(heap)
    while extraStudents > 0:
        ratio, p, t = heappop(heap)
        p += 1
        t += 1
        heappush(heap,(((p/t)-(p+1)/(t+1)),p,t))
        extraStudents -= 1
    return sum(p/t for ratio,p,t in heap) / len(heap)

# Create a heap that uses negative numbers so that the highest value is first
# We want to store the highest impact values for each class after adding 1
# extra student compared to the current pass ratio.
# For each extra student, pop the highest impact, and add its new impact value
# after adding another extra student to that class.
# This will create a heap that will maximise the average pass ratio.
# O(n + nlogn), O(n) space 
classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
maximumAverageRatio = maxAverageRatio(classes,extraStudents)
print(maximumAverageRatio)
