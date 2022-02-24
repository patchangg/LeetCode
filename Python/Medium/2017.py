
def gridGame(self, grid: List[List[int]]) -> int:
    output = float(inf)
    topSum = sum(grid[0])
    botSum = 0
    for i in range(len(grid[0])):
        print(topSum,botSum,output)
        topSum -= grid[0][i]
        output = min(output,max(topSum,botSum))
        botSum += grid[1][i]
    return output

# Since there is only two rows, that means the robots can only move down once.
# So calculate the score on every index if the bot moved down to the second
# row. This will dictate the path the first robot will take to minimize the
# points the second robot will get as we mizimize the score on the top row.
# O(n), O(1) space 
grid = [[2,5,4],[1,5,1]]
secondBotScore = gridGame(grid)
print(secondBotScore)
