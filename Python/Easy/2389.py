from bisect import bisect

def answerQueries(nums, queries):
    prefixSum = [0]
    output = []
    for num in sorted(nums):
        prefixSum.append(prefixSum[-1] + num)
    for query in queries:
        output.append(bisect(prefixSum, query) - 1)
    return output

nums = [4,5,2,1]
queries = [3,10,21]
subsequences = answerQueries(nums,queries)
print(subsequences)
