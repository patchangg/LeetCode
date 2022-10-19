
def slowestKey(releaseTimes, keysPressed):
    key = keysPressed[0]
    time = releaseTimes[0]
    for i in range(1,len(releaseTimes)):
        t = releaseTimes[i] - releaseTimes[i-1]
        if t > time or (t == time and keysPressed[i] > key):
            key = keysPressed[i]
            time = t
    return key

releaseTimes = [9,29,49,50]
keysPressed = "cbcd"
longestPressedKey = slowestKey(releaseTimes,keysPressed)
print(longestPressedKey)
