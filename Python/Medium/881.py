
def numRescueBoats(people, limit):
    people.sort(reverse=True)
    l = 0
    r = len(people) - 1
    while l <= r:
        if people[l] + people[r] <= limit:
            r -= 1
        l += 1
    return l

# Sort the people from heaviest to lightest as we want to pair the heavy
# people with the light people. If the sum of the weight is greater than the
# limit, we let the heavy person go alone. O(nlogn), O(1) space
people = [1,2]
limit = 3
numBoats = numRescueBoats(people,limit)
