
def isRobotBounded(self, instructions: str) -> bool:
    x = 0
    y = 0
    dx = 0
    dy = 1
    for i in instructions:
        if i == "L":
            dx, dy = -dy,dx
        if i == "R":
            dx, dy = dy,-dx
        if i == "G":
            x = x + dx
            y = y + dy
    return (x, y) == (0, 0) or (dx, dy) != (0,1)

# Robot starts at 0,0 facing north so direction y = 1
# If the instruction is L, turn Left by changing it to -90 degrees
# If the instruction is R, turn right by changing it to 90 degrees
# If the instruction is G, move 1 in the direction it is facing
# O(n), O(1) space
instructions = "GGLLGG"
isBounded = isRobotBounded(instructions)
print(isBounded)
