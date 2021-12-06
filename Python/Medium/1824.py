
def minSideJumps(obstacles):
    dp = [1,0,1]
    for obstacle in obstacles:
        if obstacle:
            dp[obstacle - 1] = float('inf')
        for i in range(3):
            if obstacle != i + 1:
                dp[i] = min(dp[i],dp[(i+1) % 3] + 1, dp[(i+2) % 3] + 1)
    return min(dp)

# If there is a obstacle in the way, change that lane to infinity as we can't
# use it. From each position in the lane, calculate the min jumps to get to it
# Return the min amount of jumps needed. O(n), O(1) space
obstacles = [0,1,2,3,0]
minJumps = minSideJumps(obstacles)
print(minJumps)
