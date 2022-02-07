
def totalFruit(fruits):
    lastFruit = -1
    secondLastFruit = -1
    output = 0
    lastFruitCount = 0
    currentFruit = 0
    for fruit in fruits:
        if fruit in (lastFruit,secondLastFruit):
            currentFruit += 1
        else:
            currentFruit = lastFruitCount + 1

        if fruit == lastFruit:
            lastFruitCount += 1
        else:
            lastFruitCount = 1

        if fruit != lastFruit:
            secondLastFruit = lastFruit
            lastFruit = fruit

        output = max(output,currentFruit)
    return output

# Keep track of two fruits. Go through the fruits array, if a seen fruit is found
# increment the counter, if its the last fruit seen, increment that also.
# If its a new fruit, swap the last fruit with the second last fruit seen and
# change the last fruit seen to the new one. This creates a two fruit sliding
# window that records the maximum fruit in the window each pass. O(n), O(1)
# space
fruits = [1,2,1]
maxFruits = totalFruit(fruits)
print(maxFruits)
