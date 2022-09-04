
def distributeCandies(candies, num_people):
    i = 0
    c = 1
    output = [0] * num_people
    while candies != 0:
        if candies - c > 0:
            output[i] += c
            candies -= c
            c += 1
        else:
            output[i] += candies
            candies = 0
        i += 1
        if i == num_people:
            i = 0
    return output

candies = 7
num_people = 4
candyDistribution = distributeCandies(candies,num_people)
print(candyDistribution)
