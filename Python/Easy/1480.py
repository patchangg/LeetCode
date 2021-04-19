
nums = [3,1,2,10,1]
#
#def runningSum(self, nums: List[int]) -> List[int]:
s = 0
runSum = []
for i in nums:
    s += i
    runSum.append(s)

print(runSum)

#runningSum(numz)
# class Solution(object):
#     nums = [3,1,2,10,1]
#     def runningSum(self, nums):
#         s = 0
#         runSum = []
#         for i in nums:
#             if not runSum:
#                 runSum.append(i)
#                 s = i
#             else:
#                 s += i
#                 runSum.append(s)
#         return runSum
#     array = runningSum(nums)
#     print(array)
