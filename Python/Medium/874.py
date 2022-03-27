
def robotSim(commands, obstacles):
    dx = 0
    dy = 1
    output = 0
    x = 0
    y = 0
    obstacles =  set(map(tuple, obstacles))
    for command in commands:
        if command == -2:
            dx, dy = -dy, dx
        elif command == -1:
            dx, dy = dy, -dx
        else:
            for i in range(command):
                if (dx+x,dy+y) in obstacles:
                    break
                else:
                    x += dx
                    y += dy
            output = max(output,x*x+y*y)
    return output

# Simulate the robot movement based on commands
# To turn left, swap the x and y position and make y position negative
# To turn right, swap the x and y position and make x position negative
# Otherwise, move the robot one step at a time, checking if the next step
# will hit an obstacle or not. Calculate the maximum euclideanDistance after
# each movement command. O(n+m) where n is the number of commands and m is the
# maximum positive movement command, O(n) space
commands = [4,-1,3]
obstacles = []
euclideanDistance = robotSim(commands,obstacles)
print(euclideanDistance)
