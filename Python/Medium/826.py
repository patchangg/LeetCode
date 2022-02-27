
def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    jobs = sorted(zip(difficulty, profit))
    output = 0
    best = 0
    i = 0
    for skill in sorted(worker):
        while i < len(jobs) and skill >= jobs[i][0]:
            best = max(best,jobs[i][1])
            i += 1
        output += best
    return output

# Sort the arrays from smallest to largest in terms of difficulty and worker
# skill. Go through the workers, incrementing the difficulty array based
# on the profit and level they can take, taking the best job. Repeat for every
# worker. O(nlogn), O(n) space
difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
maxProfit = maxProfitAssignment(difficulty,profit,worker)
