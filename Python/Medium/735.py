
def asteroidCollision(asteroids):
    output = []

    for asteroid in asteroids:

        while output and asteroid < 0 and output[-1] > 0:
            if output[-1] == -asteroid:
                output.pop()
                break
            elif output[-1] > -asteroid:
                break
            elif output[-1] < -asteroid:
                output.pop()
        else:
            output.append(asteroid)

    return output

# Append positive asteroids to the array.
# If a negative asteroid is found, compare it to the array.
# If it is equal to the last asteroid, pop the last asteroid in the array
# and break out of the loop
# If it is less than the last asteroid, break the loop
# If it is more than the last asteroid, pop the last asteroid in the array
# If the negative asteroid destroys all the positive asteroids, put in the array
# O(n), O(n) space
asteroids = [5,10,-5]
survivors = asteroidCollision(asteroids)
print(survivors)
