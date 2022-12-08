
def rotateString(s, goal):
    for _ in range(len(s)):
        s = s[1:] + s[0]
        if s == goal:
            return True
    return False

s = "abcde"
goal = "cdeab"
canTransformStoGoal = rotateString(s,goal)
print(canTransformStoGoal)
