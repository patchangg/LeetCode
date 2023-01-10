
def findJudge(n, trust):
    judge = [-1] + [0] * n
    for a, b in trust:
        judge[a] = float(-inf)
        judge[b] += 1

    for i, j in enumerate(judge):
        if j == n - 1:
            return i

    return -1

n = 2
trust = [[1,2]]
judge = findJudge(n,trust)
print(judge)
