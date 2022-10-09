
def numWaterBottles(numBottles, numExchange):
    output = numBottles
    while numBottles >= numExchange:
        ex = numBottles // numExchange
        output += ex
        numBottles = numBottles - (ex * numExchange) + ex
    return output

numBottles = 9
numExchange = 3
numBottlesDrank = numWaterBottles(numBottles,numExchange)
print(numBottlesDrank)
