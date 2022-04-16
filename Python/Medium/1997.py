
def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
    n = len(nextVisit)
    mod = 10**9 + 7
    dp = [0] * n
    for i in range(1, n):
        dp[i] = (2 * dp[i-1] - dp[nextVisit[i-1]] + 2) % mod
    return dp[-1] % mod

# It takes i - 1 steps to reach i, 1 step to go to i, steps - nextVisit to i
# to reach i - 1 room instead of 0 then another step to move to i
# which equals to 2 * dp[i-1] - dp[nextVisit[i-1]] + 2. O(n), O(n) space
nextVisit = [0,0]
allRoomsVisited = firstDayBeenInAllRooms(nextVisit)
print(allRoomsVisited)
