
def asteroidsDestroyed(mass, asteroids):
    asteroids = sorted(asteroids)
    for asteroid in asteroids:
        if asteroid > mass:
            return False
        else:
            mass += asteroid
    return True

# Sort the asteroids then check if the asteroid can be absorbed into the planet
# otherwise the planet is destroyed. O(nlogn), O(n) space
mass = 10
asteroids = [3,9,19,5,21]
planet = asteroidsDestroyed(mass,asteroids)
print(planet)
